
$(function(){
  window.Snip = Backbone.Model.extend({
    idAttribute: "_id",
    defaults: function(){
      return {
        snip_context: "",
      };
    },
  });
  window.SnipList = Backbone.Collection.extend({
    model: Snip,
    url: "/snips",
  });
  
  window.Snips = new SnipList;
  window.SnipView = Backbone.View.extend({
    tagName: "div",
    template: _.template($("#snip-template").html()),
    initialize: function(){
      this.model.bind("change", this.render, this);
      this.model.bind("destroy", this.remove, this);
    },
    render: function(){
      alert("render");
    },
    remove: function(){
      alert("remove");
    },
  });
  window.AppView = new Window.SnipView;
});
