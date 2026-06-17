# DOC_SET_SECTION_REF_R

> Identifies the relationship between doc_set_ref and doc_section_ref. This table will replace table DOC_SET_SECTION_RELTN with introductin of new code. This table supports type 2 versioning.

**Description:** DOC SET SECTION REF RELATION  
**Table type:** REFERENCE  
**Primary key:** `DOC_SET_SECTION_REF_R_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DOC_SET_REF_ID` | DOUBLE | NOT NULL | FK→ | FK from table DOC_SET_REF |
| 4 | `DOC_SET_SECTION_REF_ID` | DOUBLE | NOT NULL | FK→ | FK FROM DOC_SET_SECTION_REF |
| 5 | `DOC_SET_SECTION_REF_R_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `DOC_SET_SECTION_SEQUENCE` | DOUBLE | NOT NULL |  | SEQUENCE |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `PREV_DOC_SET_SECTION_REF_R_ID` | DOUBLE | NOT NULL | FK→ | PREVIOUS ID - SUPPORTS TYPE 2 VERSIONING |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_SET_REF_ID` | [DOC_SET_REF](DOC_SET_REF.md) | `DOC_SET_REF_ID` |
| `DOC_SET_SECTION_REF_ID` | [DOC_SET_SECTION_REF](DOC_SET_SECTION_REF.md) | `DOC_SET_SECTION_REF_ID` |
| `PREV_DOC_SET_SECTION_REF_R_ID` | [DOC_SET_SECTION_REF_R](DOC_SET_SECTION_REF_R.md) | `DOC_SET_SECTION_REF_R_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DOC_SET_SECTION_REF_R](DOC_SET_SECTION_REF_R.md) | `PREV_DOC_SET_SECTION_REF_R_ID` |

