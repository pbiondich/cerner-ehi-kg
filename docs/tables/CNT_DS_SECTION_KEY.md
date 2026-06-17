# CNT_DS_SECTION_KEY

> Used to build data to be imported into DOC_SET_SECTION_REF

**Description:** Content Doc Set Section Key  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLOW_COMMENT_IND` | DOUBLE | NOT NULL |  | Determines if comments may be written against the documentation set section. |
| 3 | `CNT_DS_SECTION_KEY_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the CNT_DS_SECTION_KEY table. |
| 4 | `CNT_DS_SECTION_KEY_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of doc set in conjunction with version_dt_tm column |
| 5 | `DOC_SET_SECTION_DESCRIPTION` | VARCHAR(250) | NOT NULL |  | A description of a documentation set section. |
| 6 | `DOC_SET_SECTION_INSTRUCTION` | VARCHAR(2000) | NOT NULL |  | This is instructional content used to assist with entering data related to the elements contained within the section. |
| 7 | `DOC_SET_SECTION_NAME` | VARCHAR(40) | NOT NULL |  | Name of the doc set |
| 8 | `DOC_SET_SECTION_NAME_KEY` | VARCHAR(40) | NOT NULL |  | The name value of DOC_SET_SECTION_NAME in all CAPS with no spaces. |
| 9 | `DOC_SET_SECTION_REF_ID` | DOUBLE |  | FK→ | When the configuration is imported from from .xml/.czf to this table, ithis column will be populated with a null value. When Bedrock tool maps this record, it will be updated to the parent row from DOC_SET_SECTION_REF. |
| 10 | `EVENT_CD` | DOUBLE | NOT NULL |  | Type of doc set section as defined in event code model |
| 11 | `EVENT_CD_CKI` | VARCHAR(255) | NOT NULL |  | Cerner Knowledge Index for Event code |
| 12 | `EVENT_CD_CONCEPT_CKI` | VARCHAR(255) | NOT NULL |  | Cerner Knowledge Index for Event code concept |
| 13 | `EVENT_CD_DISPLAY_NAME` | VARCHAR(40) | NOT NULL |  | The display name from CODE_VALUE for the EVENT_CD. |
| 14 | `EVENT_CD_UID` | VARCHAR(100) | NOT NULL |  | UID(unique identification) number which is used in versioning of event cd in conjunction with version_dt_tm column |
| 15 | `EVENT_SET_NAME` | VARCHAR(100) | NOT NULL |  | The Event Set Name |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | Date and time when this record was updated, used in versioning of the doc set section in conjunction with UID column. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_SET_SECTION_REF_ID` | [DOC_SET_SECTION_REF](DOC_SET_SECTION_REF.md) | `DOC_SET_SECTION_REF_ID` |

