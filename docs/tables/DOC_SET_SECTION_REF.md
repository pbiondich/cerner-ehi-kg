# DOC_SET_SECTION_REF

> Defines documentation set section.

**Description:** Documentation Set Section Reference  
**Table type:** REFERENCE  
**Primary key:** `DOC_SET_SECTION_REF_ID`  
**Columns:** 18  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLOW_COMMENT_IND` | DOUBLE | NOT NULL |  | Determines if comments may be written against the documentation set section. |
| 3 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 4 | `DOC_SET_SECTION_DESCRIPTION` | VARCHAR(250) |  |  | A description of a documentation set section. |
| 5 | `DOC_SET_SECTION_INSTRUCTION` | VARCHAR(2000) |  |  | This is instructional content used to assist with entering data related to the elements contained within the section. |
| 6 | `DOC_SET_SECTION_NAME` | VARCHAR(40) | NOT NULL |  | The name of the event set |
| 7 | `DOC_SET_SECTION_NAME_KEY` | VARCHAR(40) | NOT NULL |  | The name value of DOC_SET_SECTION_NAME in all CAPS with no spaces. |
| 8 | `DOC_SET_SECTION_REF_ID` | DOUBLE | NOT NULL | PK | Identifies a specific version of a documentation set section related to the SECTION_REF_ID |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EVENT_CD` | DOUBLE | NOT NULL |  | Type of doc set section as defined in event code model |
| 11 | `EVENT_SET_NAME` | VARCHAR(100) | NOT NULL |  | The Event Set Name |
| 12 | `PREV_DOC_SET_SECTION_REF_ID` | DOUBLE | NOT NULL | FK→ | Previous DOC_SET_SCTION_REF ID. Used for type 2 versioning |
| 13 | `SECTION_REF_ID` | DOUBLE | NOT NULL |  | Identifies a documentation set section across all versions of the section. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_DOC_SET_SECTION_REF_ID` | [DOC_SET_SECTION_REF](DOC_SET_SECTION_REF.md) | `DOC_SET_SECTION_REF_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CNT_DS_SECTION_KEY](CNT_DS_SECTION_KEY.md) | `DOC_SET_SECTION_REF_ID` |
| [DOC_SET_ELEMENT_REF](DOC_SET_ELEMENT_REF.md) | `DOC_SET_SECTION_REF_ID` |
| [DOC_SET_SECTION_REF](DOC_SET_SECTION_REF.md) | `PREV_DOC_SET_SECTION_REF_ID` |
| [DOC_SET_SECTION_REF_R](DOC_SET_SECTION_REF_R.md) | `DOC_SET_SECTION_REF_ID` |
| [ONC_TASK_SENT_RELTN](ONC_TASK_SENT_RELTN.md) | `DOC_SET_SECTION_ID` |

