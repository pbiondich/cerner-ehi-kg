# CCR_SECTION_CRITERIA

> Specifies the type of data in a section.

**Description:** Section Criteria  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CRITERIA_TYPE_FLAG` | DOUBLE | NOT NULL |  | 0 = NO VALUE, 1 = Event SET, 2 = FORM REF Description, 3 = Non Med Catalog, 4 = Originally Ordered AS, 5 = DATE TYPE |
| 4 | `CRITERIA_VALUE_TXT` | VARCHAR(255) | NOT NULL |  | Criteria Value Text |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `PREV_SECTION_CRITERIA_ID` | DOUBLE | NOT NULL |  | Previous Section Criteria ID - required for versioning |
| 7 | `SECTION_CRITERIA_ID` | DOUBLE | NOT NULL |  | Identifies the current section criteria. PK for this table |
| 8 | `SECTION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the section this criteria defines. |
| 9 | `SEQUENCE_NBR` | DOUBLE | NOT NULL |  | Sequence Number |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SECTION_ID` | [CCR_SECTION](CCR_SECTION.md) | `SECTION_ID` |

