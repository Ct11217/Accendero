import React, { Component } from "react"
import Modal from "./components/Modal";
import axios from "axios";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            itemList: [],
            modal: false,
            activeItem: {
                item: "",
                item_desc: "",
                new_entry: false
            },
        };
    }

  componentDidMount() {
  this.refreshList();
  }

  refreshList = () => {
  axios
    .get("/api/items/")
    .then((res) => this.setState({ itemList: res.data }))
    .catch((err) => console.log(err));
        console.log(this.state.itemList)
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    this.toggle();
    console.log(item)
    if (!item.new_entry)
    {
    axios
        .put(`/api/items/${item.item}/`, item)
        .then((res) => this.refreshList());
    return;
    }
    axios
        .post("/api/items/", item)
        .then((res) => this.refreshList());
  };

  handleDelete = (item) => {
    axios
        .delete(`/api/items/${item.item}`, item)
        .then((res) => this.refreshList())
  };

  createItem = () => {
    const item = { item: "", item_desc: "", new_entry: true};

    this.setState({ activeItem: item, modal: !this.state.modal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };

renderItems = () => {
    return this.state.itemList.map((item) => (
      <li
        key={item.item}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={"item-title mr-2"}
          title={item.item_desc}
        >
          {item.item}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.handleDelete(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-black text-uppercase text-center my-4">Forecasting app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add Item
                </button>
              </div>
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
            <Modal
                activeItem={this.state.activeItem}
                toggle={this.toggle}
                onSave={this.handleSubmit}
            />
          ) : null}
      </main>
    );
  }
}

export default App;
