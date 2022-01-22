import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Item</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
            {this.state.activeItem.new_entry ? (
                <Input
                type="number"
                name="item"
                value={this.state.activeItem.item}
                onChange={this.handleChange}
                placeholder="Enter Item Number"
              />
            ) :
              <Label for="item-item">Item Number: {this.state.activeItem.item}</Label>}
            </FormGroup>
            <FormGroup>
              <Label for="item_desc">Description</Label>
              <Input
                type="text"
                name="item_desc"
                value={this.state.activeItem.item_desc}
                onChange={this.handleChange}
                placeholder="Enter Item description"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}