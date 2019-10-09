var converter = Markdown.getSanitizingConverter();
var editor = new Markdown.Editor(converter, "-content");

var help = function () { alert("Do you need help?"); }

var editor = new Markdown.Editor(converter, "", { handler: help });

var $dialog = $('#insertImageDialog').dialog({ 
				autoOpen: false,
				closeOnEscape: false,
				open: function(event, ui) { $(".ui-dialog-titlebar-close").hide(); }
});

var $loader = $('span.loading-small', $dialog);
var $url = $('input[type=text]', $dialog);
var $file = $('input[type=file]', $dialog);

editor.hooks.set('insertImageDialog', function(callback) {

// dialog functions
var dialogInsertClick = function() {                                      
		callback($url.val().length > 0 ? $url.val() : null);
		dialogClose();
};

var dialogCancelClick = function() {
		dialogClose();
		callback(null);
};

var dialogClose = function() {
		// clean up inputs
		$url.val('');
		$file.val('');
		$dialog.dialog('close');
};

// set up dialog button handlers
$dialog.dialog( 'option', 'buttons', { 
		'Insert': dialogInsertClick, 
		'Cancel': dialogCancelClick 
});

var uploadStart = function() {
		$loader.show();
};

var uploadComplete = function(response) {
		$loader.hide();
		if (response.success) {
				callback(response.imagePath);
				dialogClose();
		} else {
				alert(response.message);
				$file.val('');
		}
};

// upload
$file.unbind('change').ajaxfileupload({
		action: $file.attr('data-action'),
		onStart: uploadStart,
		onComplete: uploadComplete
});

// open the dialog
$dialog.dialog('open');

return true; // tell the editor that we'll take care of getting the image url
});

editor.run();
