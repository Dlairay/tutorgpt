import topic
import keywordgenerator
import youtubetool
import time 

def main():
    pdf_path = "olevel4048mathsyllabus.pdf"  # Replace with your PDF file path
    topics = topic.extract_topics_from_pdf(pdf_path)
    print("topic extraction completed")
    print("summarising syllabus requirements with chat gpt...")
    keywords_list = keywordgenerator.generate_keyword_list(topics)
    print("summary completed")
    video_library = youtubetool.retrieve_videos(keywords_list)


    return video_library

print(main())










