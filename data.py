import json

class Data:

    def __init__(self):
        self.datas = [
  {
    "date": "2018-09-30",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-01",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-02",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-03",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-04",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-05",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-06",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-07",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-08",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-09",
    "counts": [
      1,
      0,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-10",
    "counts": [
      1,
      1,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-11",
    "counts": [
      1,
      1,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-12",
    "counts": [
      1,
      1,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-13",
    "counts": [
      1,
      2,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-14",
    "counts": [
      2,
      2,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-15",
    "counts": [
      2,
      2,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-16",
    "counts": [
      2,
      2,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-17",
    "counts": [
      1,
      5,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-18",
    "counts": [
      1,
      6,
      0,
      0,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-19",
    "counts": [
      0,
      9,
      2,
      1,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-20",
    "counts": [
      0,
      9,
      2,
      1,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-21",
    "counts": [
      0,
      9,
      3,
      2,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-22",
    "counts": [
      0,
      9,
      3,
      2,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-23",
    "counts": [
      0,
      9,
      3,
      2,
      0,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-24",
    "counts": [
      0,
      13,
      3,
      1,
      1,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-25",
    "counts": [
      1,
      10,
      9,
      1,
      1,
      0
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-26",
    "counts": [
      1,
      10,
      4,
      1,
      0,
      10
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-27",
    "counts": [
      1,
      10,
      1,
      1,
      0,
      13
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-28",
    "counts": [
      1,
      9,
      2,
      1,
      0,
      13
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-29",
    "counts": [
      1,
      9,
      2,
      1,
      0,
      13
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-30",
    "counts": [
      1,
      9,
      2,
      1,
      0,
      13
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  },
  {
    "date": "2018-10-31",
    "counts": [
      1,
      6,
      4,
      3,
      0,
      15
    ],
    "state_names": [
      "Analysis Active",
      "Analysis Done",
      "Dev Active",
      "Dev Done",
      "Testing",
      "Done"
    ],
    "state_uuids": [
      "fake-uuid-a",
      "fake-uuid-b",
      "fake-uuid-c",
      "fake-uuid-d",
      "fake-uuid-e",
      "fake-uuid-f"
    ]
  }
]

    def add_book(self, title, author):
        new_book = {}
        new_book["Title"] = title
        new_book["Author"] = author
        self.books.append(new_book)
        print("Book: {0}".format(new_book))
        return json.dumps(new_book)

    def del_book(self, title):
        found = False
        for idx, book in enumerate(self.books):
            if book["Title"] == title:
                index = idx
                found = True
                del self.books[idx]
        print("books: {0}".format(json.dumps(self.books)))
        return found

    def get_all_books(self):
        return self.datas

    def json_list(self):
        return json.dumps(self.datas)
