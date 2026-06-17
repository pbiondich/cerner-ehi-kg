# MLTM_UNITS

> Contains a listing of units of measurement related to drugs (milligram, milliliter, milliequivalent, gram, etc.), along with an abbreviation and a unique identifier for each unit.

**Description:** Units of measurement related to drugs with an abbreviation and unique ID units.  
**Table type:** REFERENCE  
**Primary key:** `UNIT_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `UNIT_ABBR` | VARCHAR(30) |  |  | This field contains an abbreviation for each unit of measurement in Multum's databases. (For example: ml, mg, gm) |
| 2 | `UNIT_CD` | DOUBLE | NOT NULL |  | Multum Unit Code - Unit of Measure |
| 3 | `UNIT_DESCRIPTION` | VARCHAR(255) |  |  | This field contains a textual description of each unit of measurement used in Multum's databases. For example: (milliliter, milligram, gram) |
| 4 | `UNIT_ID` | DOUBLE | NOT NULL | PK | This field contains a unique code for each unit of measurement used in Multum's databases. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MLTM_BCB_DRC_UNITS](MLTM_BCB_DRC_UNITS.md) | `UNIT_ID` |

