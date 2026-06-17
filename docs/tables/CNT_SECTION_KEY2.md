# CNT_SECTION_KEY2

> SECTION KEY

**Description:** CNT SECTION KEY  
**Table type:** REFERENCE  
**Primary key:** `CNT_SECTION_KEY2_ID`  
**Columns:** 12  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_SECTION_KEY2_ID` | DOUBLE | NOT NULL | PK | Sequence generated ID PRIMARY KEY |
| 2 | `DCP_SECTION_REF_ID` | DOUBLE | NOT NULL |  | Unique identifier for each individual form section |
| 3 | `SECTION_DEFINITION` | VARCHAR(200) |  |  | Textual definition of the section |
| 4 | `SECTION_DESCRIPTION` | VARCHAR(200) |  |  | Textual description of the section. This is displayed in the navigator when a form is charted. |
| 5 | `SECTION_INTERNAL_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for domain generated Section |
| 6 | `SECTION_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for Section |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `VERSION_DT_TM` | DATETIME |  |  | Stored version of the section |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CNT_INPUT](CNT_INPUT.md) | `CNT_SECTION_KEY2_ID` |
| [CNT_INPUT_KEY](CNT_INPUT_KEY.md) | `CNT_SECTION_KEY2_ID` |
| [CNT_PF_SECTION_R](CNT_PF_SECTION_R.md) | `CNT_SECTION_KEY2_ID` |
| [CNT_SECTION](CNT_SECTION.md) | `CNT_SECTION_KEY2_ID` |
| [CNT_SECTION_DTA_R](CNT_SECTION_DTA_R.md) | `CNT_SECTION_KEY_ID` |

