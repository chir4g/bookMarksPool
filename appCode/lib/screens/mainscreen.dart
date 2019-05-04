import 'package:flutter/material.dart';
import '../wgts/tile.dart';
import 'bookmark_list.dart';
import '../utils/dbhelper.dart';

class MainScreen extends StatefulWidget {
  _MainScreenState createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  final _formKey = GlobalKey<FormState>();
  final markController = TextEditingController();
  final urlController = TextEditingController();
  final List<CardMaker> _mybooks = <CardMaker>[];
  final dbHelper = DatabaseHelper.instance;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Stack(fit: StackFit.expand, children: <Widget>[
        Image(
          image: AssetImage('assets/img/background.jpg'),
          fit: BoxFit.cover,
          color: Colors.black87,
          colorBlendMode: BlendMode.lighten,
        ),
        Column(mainAxisAlignment: MainAxisAlignment.center, children: <Widget>[
          Form(
            key: _formKey,
            child: Theme(
              data: ThemeData(
                  brightness: Brightness.dark,
                  primarySwatch: Colors.teal,
                  inputDecorationTheme: InputDecorationTheme(
                      labelStyle: TextStyle(
                    color: Colors.white,
                    fontSize: 16.0,
                  ))),
              child: Container(
                child: Column(
                  children: <Widget>[
                    Padding(
                      padding: EdgeInsets.only(left: 10.0, top: 150.0),
                      child: TextFormField(
                        controller: markController,
                        decoration: InputDecoration(labelText: "BookMark Name"),
                        validator: (value) {
                          if (value.isEmpty) {
                            return 'Please Enter valid name';
                          }
                        },
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.only(left: 8.0),
                      child: TextFormField(
                        controller: urlController,
                        decoration: InputDecoration(labelText: "Url"),
                        validator: (value) {
                          if (value.isEmpty || !value.contains('.')) {
                            return "Url doesn't exist";
                          }
                          if (value.substring(0, 8) != 'https://') {
                            return "Please Enter the url as https://google.com";
                          }
                        },
                      ),
                    ),
                    Padding(
                        padding: const EdgeInsets.symmetric(vertical: 16.0),
                        child: MaterialButton(
                          height: 50,
                          minWidth: 120,
                          color: Colors.teal,
                          textColor: Colors.white,
                          child: Icon(Icons.arrow_right),
                          splashColor: Colors.white,
                          onPressed: () {
                            // Validate will return true if the form is valid, or false if
                            // the form is invalid.
                            if (_formKey.currentState.validate()) {
                              CardMaker card = new CardMaker(
                                  bookmark: markController.text,
                                  url: urlController.text);
                              _mybooks.add(card);
                              _insert(markController.text, urlController.text);
                              markController.clear();
                              urlController.clear();
                            }
                          },
                        )),
                  ],
                ),
              ),
            ),
          )
        ]),
      ]),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          queryRows();
          var route = new MaterialPageRoute(
              builder: (BuildContext context) =>
                  BookmarkListViewer(bookMarkList: _mybooks));
          Navigator.of(context).push(route);
        },
        child: Icon(Icons.book),
      ),
    );
  }

  void _insert(String mark, String url) async {
    Map<String, dynamic> row = {
      DatabaseHelper.columnmark: mark,
      DatabaseHelper.columnurl: url
    };
    final id = await dbHelper.insert(row);
    print('inserted row id: $id');
  }

  void queryRows() {
    var values = dbHelper.queryAllRows();
    values.then((onValue){
      print(onValue);
    });
}
}