# INPUT_FORM_DEFINITION

> Contains the components of an input form, including input groups and input controls

**Description:** Input Form Definition  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CMPNT_HEIGHT` | DOUBLE |  |  | The height that this input form component should be displayed |
| 2 | `CMPNT_LEFT` | DOUBLE |  |  | The left value for displaying this input form component. This column is only populated when the user has re-positioned the form, i.e. Autolayout Ind = 0 |
| 3 | `CMPNT_REPEAT_IND` | DOUBLE |  |  | An indicator of whether or not this input form component is repeating |
| 4 | `CMPNT_TOP` | DOUBLE |  |  | The top value for displaying this input form component. This column is only populated when the user has re-positioned the form, i.e. Autolayout Ind = 0 |
| 5 | `CMPNT_WIDTH` | DOUBLE |  |  | The width for displaying this input form component. This column is only populated when the user has re-positioned the form, i.e. Autolayout Ind = 0 |
| 6 | `COLUMN_HEADING` | VARCHAR(100) |  |  | The column heading to be used in the listview for this input form component. Only used for repeating forms |
| 7 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 8 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 9 | `CREATE_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 10 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 11 | `FIELD_PROMPT` | VARCHAR(100) |  |  | The prompt to be used when the component appears on this input form |
| 12 | `GROUP_CD` | DOUBLE | NOT NULL |  | The input group associated with this input form |
| 13 | `GROUP_REFERENCE_ID` | DOUBLE | NOT NULL |  | Defines a unique Row in the GROUP_REFERENCE table. Can be treated like a Foreign Key |
| 14 | `GROUP_VERSION_NBR` | DOUBLE |  |  | A reference (foreign key) to the group_reference table indicating the version number of the group that this input form component belongs to, if applicable |
| 15 | `INPUT_FORM_CD` | DOUBLE | NOT NULL | FK→ | The input form that this component is associated with |
| 16 | `INPUT_FORM_DEF_SEQ` | DOUBLE | NOT NULL |  | The sequence that this input form component should be displayed (and accepted) on the form |
| 17 | `INPUT_FORM_REFERENCE_ID` | DOUBLE | NOT NULL |  | Defines a unique row in the INPUT_FORM_REFERENCE table. Can be treated like a Foreign Key. |
| 18 | `INPUT_FORM_VERSION_NBR` | DOUBLE | NOT NULL | FK→ | The version number of the input form associated with this component |
| 19 | `ONLINE_ITEM_DEFINITION_ID` | DOUBLE | NOT NULL |  | Defines a unique row in the ONLINE_ITEM_DEFINITION Table. Can be treated like a Foreign Key. |
| 20 | `ONLINE_ITEM_VERSION_NBR` | DOUBLE |  | FK→ | A reference (foreign key) to the online_item_definition table indicating the version number of the input control component of this form |
| 21 | `PROMPT_LEFT` | DOUBLE |  |  | The left position of the component on the form. |
| 22 | `PROMPT_TOP` | DOUBLE |  |  | The top position of the component on the form. |
| 23 | `REQUIRED_FLAG` | DOUBLE |  |  | An indicator of whether this component of the input form is required |
| 24 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the online_item_definition table indicating the input control component of this form |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INPUT_FORM_CD` | [INPUT_FORM_REFERENCE](INPUT_FORM_REFERENCE.md) | `INPUT_FORM_CD` |
| `INPUT_FORM_VERSION_NBR` | [INPUT_FORM_REFERENCE](INPUT_FORM_REFERENCE.md) | `INPUT_FORM_VERSION_NBR` |
| `ONLINE_ITEM_VERSION_NBR` | [ONLINE_ITEM_DEFINITION](ONLINE_ITEM_DEFINITION.md) | `ONLINE_ITEM_VERSION_NBR` |
| `TASK_ASSAY_CD` | [ONLINE_ITEM_DEFINITION](ONLINE_ITEM_DEFINITION.md) | `TASK_ASSAY_CD` |

