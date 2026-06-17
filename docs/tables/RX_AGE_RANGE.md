# RX_AGE_RANGE

> Reference data for definition of age ranges for use in pharmacy solutions.

**Description:** Pharmacy Age Range  
**Table type:** REFERENCE  
**Primary key:** `RX_AGE_RANGE_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPLAY_TXT` | VARCHAR(100) | NOT NULL |  | The text that gets displayed on the screen that describes this age range. |
| 2 | `FROM_AGE_IN_DAYS` | DOUBLE | NOT NULL |  | Number of days that is the lowest end of the age range. |
| 3 | `FROM_AGE_NBR` | DOUBLE | NOT NULL |  | The lowest end of the age range expressed in terms of FROM_AGE_UNIT_CD. |
| 4 | `FROM_AGE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measurement in which the lowest value of the age range is specified. |
| 5 | `RX_AGE_RANGE_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RX_AGE_RANGE table. |
| 6 | `TO_AGE_IN_DAYS` | DOUBLE | NOT NULL |  | Number of days that is the highest end of the age range. |
| 7 | `TO_AGE_NBR` | DOUBLE | NOT NULL |  | The highest end of the age range expressed in terms of TO_AGE_UNIT_CD. |
| 8 | `TO_AGE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measurement in which the highest value of the age range is specified. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_MED_ORD_DETAIL](RX_MED_ORD_DETAIL.md) | `RX_AGE_RANGE_ID` |

