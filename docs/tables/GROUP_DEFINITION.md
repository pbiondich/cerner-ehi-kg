# GROUP_DEFINITION

> Identifies a component of an input group -- used by the Form Builder.

**Description:** Group Definition  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLUMN_HEADING` | VARCHAR(100) |  |  | The column heading that will be used in the listview for a repeating group. |
| 2 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table. |
| 3 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table. |
| 4 | `CREATE_ID` | DOUBLE |  |  | The person responsible for inserting this row on the table |
| 5 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 6 | `FIELD_PROMPT` | VARCHAR(100) |  |  | The prompt to be used when this component appears in this group. |
| 7 | `GROUP_CD` | DOUBLE | NOT NULL |  | A reference to the code_value table indicating the group being defined |
| 8 | `GROUP_CMPNT_LEFT` | DOUBLE |  |  | The left position of the component within the group. This column is only filled out if the form has been re-positioned. |
| 9 | `GROUP_CMPNT_TOP` | DOUBLE |  |  | The top position of the component within the group. This column is only filled out if the form has been re-positioned. |
| 10 | `GROUP_DEF_SEQ` | DOUBLE | NOT NULL |  | The sequence of this component within the group. |
| 11 | `GROUP_REFERENCE_ID` | DOUBLE | NOT NULL |  | This is a unique value from the GROUP_REFERENCE table. It will be considered a Foreign Key value. |
| 12 | `GROUP_VERSION_NBR` | DOUBLE | NOT NULL |  | A reference (foreign key) to the group_reference table identifying the version number of the input form group associated with this group component. |
| 13 | `ONLINE_ITEM_DEFINITION_ID` | DOUBLE | NOT NULL |  | This is a unique value for a row in the ONLINE_ITEM_DEFINITION_ID table. It will be treated like a Foreign Key value. |
| 14 | `ONLINE_ITEM_VERSION_NBR` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the online_item_definition table indicating the version number of the input control component of this group. |
| 15 | `REPEAT_IND` | DOUBLE |  |  | An indicator of whether or not this is a repeating group. |
| 16 | `REQUIRED_FLAG` | DOUBLE |  |  | An indicator of whether or not this input group component is required within the input group |
| 17 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the discrete_task_assay table identifying the input control component of this group. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ONLINE_ITEM_VERSION_NBR` | [ONLINE_ITEM_DEFINITION](ONLINE_ITEM_DEFINITION.md) | `ONLINE_ITEM_VERSION_NBR` |
| `TASK_ASSAY_CD` | [ONLINE_ITEM_DEFINITION](ONLINE_ITEM_DEFINITION.md) | `TASK_ASSAY_CD` |

