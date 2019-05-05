import 'package:flutter/material.dart';
import '../wgts/tile.dart';
import '../utils/dbhelper.dart';

class BookmarkListViewer extends StatefulWidget {
  final List<CardMaker> bookMarkList;
  final dbHelper = DatabaseHelper.instance;

  BookmarkListViewer({Key key, @required this.bookMarkList}) : super(key: key);

  _BookmarkListViewerState createState() => _BookmarkListViewerState();
}

class _BookmarkListViewerState extends State<BookmarkListViewer> {
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Your BookMarks"),
        ),
        body: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            Flexible(
              child: ListView.separated(
                padding: EdgeInsets.all(8.0),
                separatorBuilder: (_,index) => Divider(),
                itemBuilder: (_, int index) => widget.bookMarkList[index],
                itemCount: widget.bookMarkList.length,
              ),
            ),
          ],
        ),
        floatingActionButton: FloatingActionButton(
          onPressed: () {
            widget.dbHelper.drop().then((onValue){
              print("$onValue");
            });
          },
        ),
        );
  }
}
