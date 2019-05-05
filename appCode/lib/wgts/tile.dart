import 'package:flutter/material.dart';
import 'package:url_launcher/url_launcher.dart';

class CardMaker extends StatelessWidget {
  final String bookmark;
  final String url;

  CardMaker({this.bookmark, this.url});

  Widget build(BuildContext context) {

    _launchURL() async {
  var url = this.url;
  if (await canLaunch(url)) {
    await launch(url);
  } else {
    throw 'Could not launch $url';
  }
}


    return GestureDetector(
      onTap: (){
        print("Tapped");
        _launchURL();
      },
      child: Container(
      padding: EdgeInsets.all(3.0),
      child: Column(
        children: <Widget>[
          Align(
            alignment: Alignment.topLeft,
            child: Text(
              bookmark,
              style: TextStyle(
                fontSize: 20.0,
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(top: 20.0),
          ),
          Align(
            alignment: Alignment.topLeft,
              child: Text(
              url,
              style: TextStyle(
                fontSize: 20.0,
              ),
            ),
          ),
        ],
      ),
    )
    );
  }
}
