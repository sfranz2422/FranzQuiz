quiz1 = [{"question":"What are the last 4 characters of a file that contains nothing but statements like this?", "answer":".css", "image":"flower.png"},{"question":"Type the first 3 characters of CSS code that specifies styling for paragraphs.", "answer":"p{","image":""}]


quiz2 = [{"question":"What is the capital of the US?", "answer":"dc","image":"flower.png"},{"question":"What is my name?", "answer":"Franz","image":"flower.png"},{"question":"What is the year?", "answer":"2025","image":"flower.png"}]



links_and_buttons =[{'question': 'Fill in the blank for the first line that styles a link that the user has previously clicked.', 'answer': 'visited', 'image': 'links_buttons_9.png',"starter":""},{'question': 'Make an empty anchor tag without any attributes.  Include the opening and closing tag.', 'answer': '<a></a>', 'image': '',"starter":""}, {'question': 'Type the name of the attribute that contains the link address.  It is 4 letters long.', 'answer': 'href', 'image': '',"starter":""}, {'question': 'Create an anchor tag that links to example.com and has a title attribute with a value of Example.  The link text should also be Example.', 'answer': '<a href="example.com" title="Example">Example</a>', 'image': '',"starter":""}, {'question': 'Create a css rule for an anchor tag.  Leave the rule empty.', 'answer': 'a{}', 'image': '',"starter":""}, {'question': 'Create a css rule for an anchor tag that makes the foreground color blue.', 'answer': 'a{color:blue;}', 'image': '',"starter":""}, {'question': 'Create an empty css rule for an a tag that has uses the hover pseudo-class', 'answer': 'a:hover{}', 'image': '',"starter":""}, {'question': 'Fill in the blank so the anchor tag is orange when the user hovers over the link', 'answer': 'orange', 'image': 'links_buttons_8.png',"starter":""}, {'question': 'Fill in the blank to complete the first line for styling a link when it is moused over or hovered.', 'answer': 'hover', 'image': 'links_buttons_9.png',"starter":""}, {'question': 'Fill in the blank for the first line that styles a link when the user clicks it.', 'answer': 'active', 'image': 'links_buttons_9.png',"starter":""}]


basic_html = [
  {
    "question": "Create an unordered list with the following list items: 'Apple', 'Banana', 'Cherry'.",
    "answer": "<ul><li>Apple</li><li>Banana</li><li>Cherry</li></ul>",
    "image": "",
    "starter":"""
    <ul>
      <li>Apple</li>
      <li>Banana</li>
      <li>      </li>
    </ul>
    """
  },
  {
    "question": "Create a paragraph with the text 'This is a simple paragraph.'.",
    "answer": "<p>This is a simple paragraph.</p>",
    "image": "","starter":""
  },
  {
    "question": "Write the HTML to create an ordered list with the following items: 'First', 'Second', 'Third'.",
    "answer": "<ol><li>First</li><li>Second</li><li>Third</li></ol>",
    "image": "",
    "starter":""
  },
  {
    "question": "Create a hyperlink that opens in a new tab and links to 'https://example.com'.",
    "answer": "<a href='https://example.com' target='_blank'>Visit Example</a>",
    "image": "",
    "starter":""
  },
  {
    "question": "Create a heading (h1) with the text 'Welcome to My Website'.",
    "answer": "<h1>Welcome to My Website</h1>",
    "image": "",
    "starter":""
  },
  {
    "question": "Create a line break in your page using HTML.",
    "answer": "<br>",
    "image": "",
    "starter":""
  },
  {
    "question": "Write the HTML to create a heading (h2) called 'Services'.",
    "answer": "<h2>Services</h2>",
    "image": "",
    "starter":""
  },
  {
    "question": "Create an image with the source 'https://example.com/logo.png' and the alt text 'Company Logo'.",
    "answer": "<img src='https://example.com/logo.png' alt='Company Logo'>",
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/HTML5_Logo.svg/1280px-HTML5_Logo.svg/1280px-HTML5_Logo.svg.png",
    "starter":""
  },
  {
    "question": "Create an unordered list with the following items: 'HTML', 'CSS', 'JavaScript'.",
    "answer": "<ul><li>HTML</li><li>CSS</li><li>JavaScript</li></ul>",
    "image": "",
    "starter":""
  },

]


python_loops = [
  {
    "question": "Complete the for-loop that prints numbers from 1 to 5.\nUse 'i' as the variable.\nUse the tab key for indentation.",
    "answer": "for i in range(1, 6):\n\tprint(i)",
    "image": "","starter":"for i in range(______):\n\t"
    
  },
  {
    "question": "Use a for-loop to print each character in the string 'Python'.\n Use 'char' as the target variable\nUse the tab key for indentation.",
    "answer": "for char in 'Python':\n\t print(char)",
    "image": "","starter":""
  },
  {
    "question": "Write a loop that prints only even numbers from 2 to 10.\nUse 'i' as the variable.\nUse the tab key for indentation.",
    "answer": "for i in range(2, 11, 2):\n\t print(i)",
    "image": "","starter":"for i in range(__,__,__):\n\t"
  },
  {
    "question": "Use a while-loop to print numbers from 10 down to 1.\nUse 'i' as the variable..\nUse the tab key for indentation.",
    "answer": "i = 10\nwhile i > 0:\n\tprint(i)\n\ti -= 1",
    "image": "","starter":"i=10\n"
  },
  {
    "question": "Write a loop that iterates through a list of numbers [3, 6, 9] and prints each number.\nThe list is saved in a variable called 'numbers'.\nUse the target variable 'num' in your for loop.\nUse the tab key for indentation.",
    "answer": "numbers = [3, 6, 9]\nfor num in numbers:\n\tprint(num)",
    "image": "","starter":"numbers = [3, 6, 9]\n"
  }
]