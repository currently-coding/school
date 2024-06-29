module.exports = async (tp) => {
  const currentFolder = tp.file.path(true).replace(tp.file.title + '.md', '');
  const newFileName = await tp.system.prompt("Enter new file name");
  const newFilePath = currentFolder + newFileName + '.md';
  
  // Check if a folder-specific template exists
  const folderTemplate = tp.file.find_tfile(currentFolder + 'FolderSpecificTemplate.md');
  const template = folderTemplate ? folderTemplate : tp.file.find_tfile("Templates/DefaultTemplate.md");
  
  await tp.file.create_new(template, newFilePath, true);
}