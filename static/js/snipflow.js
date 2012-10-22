
$(function(){
  window.SnipList = Backbone.Collection.extend({
    url: "/snips",
  });
  
  window.Snips = new SnipList;
  window.SnipView = Backbone.View.extend({
    template: _.template($("#snip-template").html()),
    initialize: function(){
      this.model.bind('change', this.render, this);
      this.model.bind('destroy', this.remove, this);
    },
    render: function(){
      $(this.el).html(this.template(this.model.toJSON()));
      return this;
    },
    remove: function(){
      $(this.el).remove();
    },
  });
  window.AppView = Backbone.View.extend({
    tagName: "div",
    initialize: function(){
      Snips.bind("reset", this.addAll, this);
      Snips.bind("all", this.render, this);
      Snips.fetch();
    },
    render: function(){
      this.addAll();
    },
    addOne: function(snip){
      var view = new SnipView({model: snip});
      $("#container").append(view.render().el);
    },
    addAll: function(){
      $("#container").html('');
      Snips.each(this.addOne);
    },
  });
  window.App = new AppView;
});
