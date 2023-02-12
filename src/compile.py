
import os

compile_list = ["index.jemdoc",
                "news.jemdoc",
                "skills.jemdoc",
                "talks.jemdoc",
                "mics.jemdoc",
                "papers.jemdoc",
                # "books.jemdoc",
                "awards.jemdoc",
                "service.jemdoc",
                "mylab.jemdoc"
                ]

os.system("python jemdoc -c mysite.conf " + " ".join(compile_list))

