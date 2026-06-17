# DOC_SET_ELEMENT_REF

> Defines a discrete input element that is used for entering data within a documentation set section.

**Description:** Documentation Set Element Reference  
**Table type:** REFERENCE  
**Primary key:** `DOC_SET_ELEMENT_ID`  
**Columns:** 20  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLOW_COMMENT_IND` | DOUBLE | NOT NULL |  | Determines if comments may be written against the documentation set section. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `DOC_SET_ELEMENT_DESCRIPTION` | VARCHAR(250) |  |  | A description of a documentation set element. |
| 5 | `DOC_SET_ELEMENT_ID` | DOUBLE | NOT NULL | PK | Identifies a documentation set element |
| 6 | `DOC_SET_ELEMENT_NAME` | VARCHAR(40) | NOT NULL |  | The name of a documentation set element. |
| 7 | `DOC_SET_ELEM_SEQUENCE` | DOUBLE | NOT NULL |  | Identifies the ordering of this element relative to other elements contained within a section. |
| 8 | `DOC_SET_SECTION_REF_ID` | DOUBLE | NOT NULL | FK→ | Identifies a specific version of a documentation set section related to the SECTION_REF_ID. |
| 9 | `ELEMENT_TYPE_CD` | DOUBLE | NOT NULL |  | Classifies this element by its functionality. Examples include 'NUMERIC' and 'CALCULATION'. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `EVENT_CD` | DOUBLE | NOT NULL |  | Type of Section as defined in the event code model. |
| 12 | `PREV_DOC_SET_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | Previous doc_set_element_id - used for type 2 versoning |
| 13 | `READ_ONLY_IND` | DOUBLE | NOT NULL |  | Specifies if data related to this element may be saved. |
| 14 | `REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates if this element is required to be populated to ensure the section it is a part of. |
| 15 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL | FK→ | Defines information that further defines this element. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_SET_SECTION_REF_ID` | [DOC_SET_SECTION_REF](DOC_SET_SECTION_REF.md) | `DOC_SET_SECTION_REF_ID` |
| `PREV_DOC_SET_ELEMENT_ID` | [DOC_SET_ELEMENT_REF](DOC_SET_ELEMENT_REF.md) | `DOC_SET_ELEMENT_ID` |
| `TASK_ASSAY_CD` | [DISCRETE_TASK_ASSAY](DISCRETE_TASK_ASSAY.md) | `TASK_ASSAY_CD` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CNT_DS_SEC_ELEMENT_KEY](CNT_DS_SEC_ELEMENT_KEY.md) | `DS_ELEMENT_REF_ID` |
| [DOC_SET_ELEMENT_REF](DOC_SET_ELEMENT_REF.md) | `PREV_DOC_SET_ELEMENT_ID` |
| [ONC_DOCSET_ELEM_DECORATOR](ONC_DOCSET_ELEM_DECORATOR.md) | `DOC_SET_ELEMENT_ID` |
| [ONC_TASK_SENT_RELTN](ONC_TASK_SENT_RELTN.md) | `DOC_SET_ELEMENT_ID` |
| [ONC_TOKEN_ELEMENT_R](ONC_TOKEN_ELEMENT_R.md) | `DOC_SET_ELEMENT_ID` |

