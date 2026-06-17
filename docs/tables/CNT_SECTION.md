# CNT_SECTION

> SECTION

**Description:** CNT SECTION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CNT_SECTION_ID` | DOUBLE | NOT NULL |  | Sequence generated ID (Value: 0.0) PRIMARY KEY |
| 3 | `CNT_SECTION_KEY2_ID` | DOUBLE | NOT NULL | FK→ | Sequence generated ID - FROM CNT_SECTION_KEY2 |
| 4 | `SECTION_CKI` | VARCHAR(50) |  |  | A unique external identifier for CKI |
| 5 | `SECTION_FLAG` | DOUBLE | NOT NULL |  | Used for determine which sections are conditional on the import not written directly to a table |
| 6 | `SECTION_HEIGHT` | DOUBLE |  |  | Height of section. |
| 7 | `SECTION_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Section |
| 8 | `SECTION_WIDTH` | DOUBLE |  |  | Width of section. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CNT_SECTION_KEY2_ID` | [CNT_SECTION_KEY2](CNT_SECTION_KEY2.md) | `CNT_SECTION_KEY2_ID` |

