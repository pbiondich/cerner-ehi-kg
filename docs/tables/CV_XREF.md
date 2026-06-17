# CV_XREF

> Reference table

**Description:** Reference table that stores information about fields in a dataset.  
**Table type:** REFERENCE  
**Primary key:** `XREF_ID`  
**Columns:** 36  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `AUDIT_FLAG` | DOUBLE |  |  | The flag that determines if a field is included in the minimum dataset (MDS). 0 = no; 1 = yes; 2 = other |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `CERN_SOURCE_FIELD_NAME` | CHAR(30) |  |  | The name of the table attribute (column) as defined in Cerner source table |
| 8 | `CERN_SOURCE_TABLE_NAME` | CHAR(30) |  |  | The source table name for Cerner. |
| 9 | `COLLECT_START_DT_TM` | DATETIME |  |  | The date and time to start collection of the registry field. |
| 10 | `COLLECT_STOP_DT_TM` | DATETIME |  |  | The date and time to stop collection of the registry field. |
| 11 | `DATASET_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key for this table. |
| 12 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 13 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 14 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 15 | `DISPLAY_FIELD_IND` | DOUBLE |  |  | Not used |
| 16 | `ELEMENT_NBR` | DOUBLE |  |  | Registry defined ordering number for the element. |
| 17 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 18 | `ERROR_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The Error Text for the Field to be displayed in Audit and/or Error Log |
| 19 | `EVENT_CD` | DOUBLE | NOT NULL |  | Matching event code, if applicable. |
| 20 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Set of codes that help to distingush between different eventsColumn |
| 21 | `FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | The code describes the data type the field belongs |
| 22 | `GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes different types of event according to "ACC" grouping e.g. history,presentation etc. |
| 23 | `REGISTRY_FIELD_NAME` | VARCHAR(100) | NOT NULL |  | Name of the Registry Field. |
| 24 | `REQD_FLAG` | DOUBLE |  |  | This sets the log level . |
| 25 | `SUB_EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | These are set of codes that identifies event types |
| 26 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | The task Assay code of the clinical event. There is a cdf_meaning associated with the "task_assay_cd" . This allows the value of an event to be retrieved from the code_value table. |
| 27 | `UPDT_APP` | DOUBLE |  |  | The application number that is responsible for the row update. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_REQ` | DOUBLE |  |  | The registered (assigned)request number for the process that inserted or updated the row. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 34 | `WARNING_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The Warning Message to be displayed in Audit or Error Log |
| 35 | `XREF_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the cv_xref table. It is an internal system assigned number. |
| 36 | `XREF_INTERNAL_NAME` | VARCHAR(100) |  |  | The internal name used to store the value for XREF_INTERNAL_NAME. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATASET_ID` | [CV_DATASET](CV_DATASET.md) | `DATASET_ID` |
| `ERROR_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `WARNING_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [CV_XREF_FIELD](CV_XREF_FIELD.md) | `XREF_ID` |
| [CV_XREF_VALIDATION](CV_XREF_VALIDATION.md) | `XREF_ID` |

