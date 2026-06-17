# INPUT_FORM_REFERENCE

> Contains the attributes of an input form used by the form builder, including description, repeating indicator, auto layout indicator, etc

**Description:** Input Form Reference  
**Table type:** REFERENCE  
**Primary key:** `INPUT_FORM_CD`, `INPUT_FORM_VERSION_NBR`  
**Columns:** 28  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 3 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 4 | `AUTO_LAYOUT_IND` | DOUBLE |  |  | An indicator of whether this form should use an automatic layout by the form builder or use the layout that the user has defined, i.e. repositioned the form |
| 5 | `CALC_RESULT_IND` | DOUBLE |  |  | NOT CURRENTLY BEING USED |
| 6 | `COLUMN_SORT_IND` | DOUBLE |  |  | An indicator of whether or not to allow column sorting in the listbox -- for repeating forms only |
| 7 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 8 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 9 | `CREATE_ID` | DOUBLE |  |  | The person responsible for inserting this row on the table |
| 10 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 11 | `DESCRIPTION` | VARCHAR(100) |  |  | A description for this input form |
| 12 | `DISPLAY` | VARCHAR(50) |  |  | A textual display for this input form. This column is not populated by mainline Surginet applications and has been deemed OBSOLETE for that solution. It is possible, however, that other applications may use the field. |
| 13 | `DISPLAY_KEY` | VARCHAR(50) |  |  | A textual display for this input form, in key form, used for retrieval purposes.This column is not populated by mainline Surginet applications and has been deemed OBSOLETE for that solution. It is possible, however, that other applications may use the field. |
| 14 | `EVENT_CD` | DOUBLE |  |  | The Event Code associated with this input form |
| 15 | `INPUT_FORM_CD` | DOUBLE | NOT NULL | PK | The primary key uniquely identifying an input form (along with version number) |
| 16 | `INPUT_FORM_REFERENCE_ID` | DOUBLE | NOT NULL |  | This column uniquely identifies a row in the table. Can be treated like a PK. |
| 17 | `INPUT_FORM_VERSION_NBR` | DOUBLE | NOT NULL | PK | The version number associated with the input form |
| 18 | `NOTE_TEMPLATE_CD` | DOUBLE |  |  | NOT CURRENTLY BEING USED -- The template to be used for comments when this input form is documented |
| 19 | `ONE_COLUMN_IND` | DOUBLE |  |  | An indicator of whether or not this input form should be displayed in one column when being documented |
| 20 | `PART_PROCESS_IND` | DOUBLE |  |  | An indicator of whether or not the version processor is currently running but not yet complete. |
| 21 | `REPEAT_IND` | DOUBLE |  |  | An indicator of whether or not this is a repeating form |
| 22 | `SYSTEM_DEFINED_FLAG` | DOUBLE |  |  | An indicator of the source of definition for this input form, i.e. Form Builder-defined, SurgiNet-defined, DCP-defined |
| 23 | `UNPROCESS_IND` | DOUBLE |  |  | An indicator of whether or not this input form has been processed by the Version Processor |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CONDITIONAL_BEHAVIOR](CONDITIONAL_BEHAVIOR.md) | `INPUT_FORM_CD` |
| [CONDITIONAL_BEHAVIOR](CONDITIONAL_BEHAVIOR.md) | `INPUT_FORM_VERSION_NBR` |
| [INPUT_FORM_DEFINITION](INPUT_FORM_DEFINITION.md) | `INPUT_FORM_CD` |
| [INPUT_FORM_DEFINITION](INPUT_FORM_DEFINITION.md) | `INPUT_FORM_VERSION_NBR` |

