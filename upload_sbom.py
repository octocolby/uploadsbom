import os
import clients.dependency_track

dependency_track_url=os.getenv("DEPENDENCY_TRACK_URL")
dependency_track_api_key=os.getenv("DEPENDENCY_TRACK_API_KEY")
project_name=os.getenv('PROJECT_NAME')
version=os.getenv('VERSION')
sbom_file=os.getenv('SBOM_FILE')
description=os.getenv('DESCRIPTION')
tags = [tag.strip() for tag in os.getenv('TAGS').split(',')]

dependency_track_client = clients.dependency_track.DependencyTrackClient(dependency_track_url, dependency_track_api_key)
print(f"Creating new project {project_name}:{version} from SBOM file {sbom_file}...")
dependency_track_client.create_project(project_name, version, sbom_file)
print(f"Tagging project {project_name}:{version} with tags {tags}...")
dependency_track_client.tag_project(project_name, version, tags, description)
print("Done 🎉")
