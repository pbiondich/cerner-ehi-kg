# DCP_FORMS_REF

> Every form has a single entry in this table that describes the form such as name and definition.

**Description:** Description of PowerForms  
**Table type:** REFERENCE  
**Primary key:** `DCP_FORM_INSTANCE_ID`  
**Columns:** 21  
**Referenced by:** 9 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DCP_FORMS_REF_ID` | DOUBLE | NOT NULL |  | Each form has a unique reference id that is used to identify the form. Each version of the form is identified by a unique instance id. |
| 4 | `DCP_FORM_INSTANCE_ID` | DOUBLE | NOT NULL | PK | Each form has a unique reference id that is used to identify the form. Each version of the form is identified by a unique instance id. |
| 5 | `DEFINITION` | VARCHAR(200) |  |  | Textual definition of the form. |
| 6 | `DESCRIPTION` | VARCHAR(200) |  |  | Textual description of the form |
| 7 | `DONE_CHARTING_IND` | DOUBLE |  |  | if this indicator is set then done charting will be allowed otherwise it is not allowed on this form |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `ENFORCE_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether to make the user enter all required fields before they are allowed to save. Without this option users can chart forms missing required fields, tasks associated with the results will be in an "In Progress" status. |
| 10 | `EVENT_CD` | DOUBLE | NOT NULL |  | Event_cd associated with this form to be used for various purposes. Currently is not used |
| 11 | `EVENT_SET_NAME` | VARCHAR(100) |  |  | specify an event set that is associated with this form to enable charting to print results. |
| 12 | `FLAGS` | DOUBLE |  |  | 1 - Do not allow any charting unless all required fields are filled out. 2 - Show form in a maximized state |
| 13 | `HEIGHT` | DOUBLE | NOT NULL |  | Height the form should be sized |
| 14 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Associates a discrete task assay with the form. Currently not used. |
| 15 | `TEXT_RENDITION_EVENT_CD` | DOUBLE | NOT NULL |  | Event code associated with the text rendered from the form. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `WIDTH` | DOUBLE | NOT NULL |  | Width the form should be sized |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (9)

| From table | Column |
|------------|--------|
| [ACT_PW_COMP](ACT_PW_COMP.md) | `DCP_FORMS_REF_ID` |
| [ACT_PW_COMP](ACT_PW_COMP.md) | `OUTCOME_FORMS_REF_ID` |
| [ORDER_CATALOG](ORDER_CATALOG.md) | `FORM_ID` |
| [PATHWAY](PATHWAY.md) | `COMP_FORMS_REF_ID` |
| [PATHWAY](PATHWAY.md) | `PW_FORMS_REF_ID` |
| [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `COMP_FORMS_REF_ID` |
| [PATHWAY_CATALOG](PATHWAY_CATALOG.md) | `PW_FORMS_REF_ID` |
| [PATHWAY_COMP](PATHWAY_COMP.md) | `DCP_FORMS_REF_ID` |
| [PATHWAY_COMP](PATHWAY_COMP.md) | `OUTCOME_FORMS_REF_ID` |

