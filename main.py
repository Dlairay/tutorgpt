import topic
import keywordgenerator
import youtubetool
import time 

def main():
    pdf_path = "olevel4048mathsyllabus.pdf"  # Replace with your PDF file path
    topics = topic.extract_topics_from_pdf(pdf_path)
    keywords_list = keywordgenerator.generate_keyword_list(topics)
    print("summarising syllabus requirements...")
    time.sleep(20)
    video_library = youtubetool.retrieve_videos(keywords_list)
    print(video_library)

    return video_library
main()


# pdf_path = "olevel4048mathsyllabus.pdf"  # Replace with your PDF file path
# topics = topic.extract_topics_from_pdf(pdf_path)
# keywords_list = keywordgenerator.generate_keyword_list(topics)
# print(keywords_list)
# keywords_list = ['Numbers operations', 'Ratio proportion', 'Percentage', 'Rate speed expressions formulae', 'Functions graphs', 'Equations inequalities', 'Set language notation', 'Matrices', 'Problems real-world contexts', 'Angles triangles polygons', 'Congruence similarity', 'Properties circles theorem trigonometry', 'Mensuration', 'Coordinate geometry', 'Vectors two dimensions', 'Problems real-world contexts', 'Data analysis', 'Probability']
# video_library = youtubetool.retrieve_videos(keywords_list)
# print(video_library)
# print("done")


