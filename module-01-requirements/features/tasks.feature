Feature: Manage To-Do Items

  Scenario: User creates a new task
    Given I am on the task list page
    When I fill in "Buy groceries" in the task title field
    And I click "Add Task"
    Then I should see "Buy groceries" in the task list

  Scenario: User marks a task as complete
    Given there is a task "Buy groceries" that is not completed
    When I click the checkbox next to "Buy groceries"
    Then the task should be marked as completed
    And it should appear with a strikethrough style

  Scenario: User deletes a task
    Given there is a task "Buy groceries" in the list
    When I click "Delete" on that task
    And I confirm the deletion
    Then "Buy groceries" should no longer appear in the list

  Scenario: User edits an existing task
    Given there is a task "Buy groceries" in the list
    When I click "Edit" on that task
    And I change the title to "Buy organic groceries"
    And I click "Save"
    Then I should see "Buy organic groceries" in the task list

  Scenario: User filters tasks to show only active items
    Given there are both completed and active tasks in the list
    When I click the "Active" filter tab
    Then I should only see tasks that are not completed

  Scenario: User tries to save a task with an empty title
    Given I am on the new task page
    When I leave the title field blank
    And I click "Add Task"
    Then I should see a validation error "Title cannot be blank."

  Scenario: Tasks are ordered by due date
    Given there are tasks with different due dates
    When I view the task list
    Then tasks should be displayed in ascending order of due date
