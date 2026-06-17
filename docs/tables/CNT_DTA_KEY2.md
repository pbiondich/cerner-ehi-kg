# CNT_DTA_KEY2

> DTA KEY

**Description:** CNT DTA KEY  
**Table type:** REFERENCE  
**Primary key:** `CNT_DTA_KEY_ID`  
**Columns:** 10  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CNT_DTA_KEY_ID` | DOUBLE | NOT NULL | PK | Sequence generated ID - primary key |
| 2 | `TASK_ASSAY_CD` | DOUBLE | NOT NULL |  | a unique code value that identifies a specific discrete task assay. |
| 3 | `TASK_ASSAY_DISP` | VARCHAR(50) |  |  | Defines the abbreviated form of the discrete task assay long description. Used in most applications to display the discrete assay task. |
| 4 | `TASK_ASSAY_UID` | VARCHAR(100) | NOT NULL |  | Unique identifier for DTA |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `VERSION_DT_TM` | DATETIME |  |  | Date the DTA we extracted from source. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (7)

| From table | Column |
|------------|--------|
| [CNT_DATA_MAP](CNT_DATA_MAP.md) | `CNT_DTA_KEY_ID` |
| [CNT_DCP_INTERP2](CNT_DCP_INTERP2.md) | `CNT_DTA_KEY_ID` |
| [CNT_DTA](CNT_DTA.md) | `CNT_DTA_KEY_ID` |
| [CNT_EQUATION](CNT_EQUATION.md) | `CNT_DTA_KEY_ID` |
| [CNT_GRID](CNT_GRID.md) | `CNT_DTA_KEY_ID` |
| [CNT_REF_TEXT](CNT_REF_TEXT.md) | `CNT_DTA_KEY_ID` |
| [CNT_SECTION_DTA_R](CNT_SECTION_DTA_R.md) | `CNT_DTA_KEY_ID` |

