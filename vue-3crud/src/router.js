import { createWebHistory, createRouter } from "vue-router";



// We create the routes as an array, each route has:

// path: the URL path where this route can be found.
// name: optional name to use when we link to this route.
// component: component to load when this route is called.



const routes =  [
  {
    path: "/",
    alias: "/tutorials",
    name: "tutorials",
    component: () => import("./components/TutorialsList")
  },
  {
    path: "/tutorials/:id",
    name: "tutorial-details",
    component: () => import("./components/Tutorial")
  },
  {
    path: "/add",
    name: "add",
    component: () => import("./components/AddTutorial")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;