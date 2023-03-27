import os

compile_list = ["index.jemdoc",
                "experiences-univ.jemdoc",
                "experiences-com.jemdoc",
                "experiences-project.jemdoc",
                "news.jemdoc",
                "skills.jemdoc",
                "talks.jemdoc",
                "edge-music.jemdoc",
                "papers.jemdoc",
                "books.jemdoc",
                "awards.jemdoc",
                "research-graphics.jemdoc",
                "engineering-ir.jemdoc",
                "engineering-software.jemdoc",
                "engineering-games.jemdoc",
                "research-edge-music.jemdoc",
                "research-nlp.jemdoc",
                "research-security.jemdoc",
                "research-bio.jemdoc",
                "research-robotics.jemdoc",
                "research-software.jemdoc",
                "music-performance.jemdoc",
                "music-composition.jemdoc",
                "social-volunteer.jemdoc",
                "social-professional-service.jemdoc",
                "advice-care.jemdoc",
                "advice-do.jemdoc",
                "advice-learn.jemdoc",
                "advice-art.jemdoc",
                "advice-interests.jemdoc",
                "social-team-construction.jemdoc",
                ]

os.system("python jemdoc.py " + " ".join(compile_list))