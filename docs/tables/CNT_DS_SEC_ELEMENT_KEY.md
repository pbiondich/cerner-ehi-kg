# CNT_DS_SEC_ELEMENT_KEY

> Used to build data to be imported into DOC_SET_ELEMENT_REF and DISCRETE_TASK_ASSAY

**Description:** Content Doc Set Section Element Key  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLOW_COMMENT_IND` | DOUBLE | NOT NULL |  | Determines if comments may be written against the documentation set section. |
| 3 | `CNT_DS_SEC_ELEMENT_KEY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CNT_DS_SEC_ELEMENT_KEY table. |
| 4 | `CNT_DS_SEC_ELEMENT_KEY_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of doc set element in conjunction with version_dt_tm column |
| 5 | `DOC_SET_ELEMENT_DESCRIPTION` | VARCHAR(250) | NOT NULL |  | A description of a documentation set element. |
| 6 | `DOC_SET_ELEMENT_NAME` | VARCHAR(40) | NOT NULL |  | The name of a documentation set element. |
| 7 | `DOC_SET_ELEM_SEQUENCE` | DOUBLE | NOT NULL |  | Identifies the ordering of this element relative to other elements contained within a section. |
| 8 | `DS_ELEMENT_REF_ID` | DOUBLE |  | FK→ | When the configuration is imported from from .xml/.czf to this table, ithis column will be populated with a null value.When Bedrock tool maps this record, it will be updated to the parent row from DOC_SET_ELEMENT_REF. |
| 9 | `ELEMENT_TYPE_CD` | DOUBLE | NOT NULL |  | Classifies this element by its functionality. Examples include 'NUMERIC' and 'CALCULATION'. |
| 10 | `ELEMENT_TYPE_CD_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of element type in conjunction with version_dt_tm column |
| 11 | `ELEMENT_TYPE_DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | Element display name |
| 12 | `ELEMENT_TYPE_MEAN_TXT` | VARCHAR(12) | NOT NULL |  | Element mean text |
| 13 | `EVENT_CD` | DOUBLE | NOT NULL |  | Type of Section as defined in the event code model. |
| 14 | `EVENT_CD_CKI` | VARCHAR(255) | NOT NULL |  | Cerner Knowledge Index for Event code |
| 15 | `EVENT_CD_CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Cerner Knowledge Index for Event code concept |
| 16 | `EVENT_CD_DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | The display name used for the event code. |
| 17 | `EVENT_CD_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of event cd in conjunction with version_dt_tm column |
| 18 | `READ_ONLY_IND` | DOUBLE | NOT NULL |  | Specifies if data related to this element may be saved. |
| 19 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates if this element is required to be populated to ensure the section it is a part of. |
| 20 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | Defines information that further defines this element. |
| 21 | `TASK_ASSAY_CD_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of task assay in conjunction with version_dt_tm column |
| 22 | `TASK_ASSAY_CKI` | VARCHAR(255) | NOT NULL |  | Cerner Knowledge Index for task assay |
| 23 | `TASK_ASSAY_DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | Display name for the Task Assay |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | Date and time when this record was updated, used in versioning of the doc set section element in conjunction with UID column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DS_ELEMENT_REF_ID` | [DOC_SET_ELEMENT_REF](DOC_SET_ELEMENT_REF.md) | `DOC_SET_ELEMENT_ID` |

