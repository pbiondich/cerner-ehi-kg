# PHARMACY_RANGE

> Pharmacy_range - Range of numbers to use for Prescription and Tracking Numbers.

**Description:** PHARMACY RANGE  
**Table type:** REFERENCE  
**Primary key:** `RANGE_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(100) |  |  | Description of range |
| 2 | `FROM_RANGE` | DOUBLE |  |  | Beginning of Range Value |
| 3 | `NEXT_VALUE` | DOUBLE |  |  | Next range value |
| 4 | `RANGE_ID` | DOUBLE | NOT NULL | PK | Unique ID identifying pharmacy range |
| 5 | `TO_RANGE` | DOUBLE |  |  | Ending of range value |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SERV_RES_EXT_PHARM](SERV_RES_EXT_PHARM.md) | `DOWNTIME_RANGE_ID` |

