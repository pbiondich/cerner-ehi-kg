# DCP_EQUATION

> This is the parent table of the equations used in the DCP Online Clin Calculator

**Description:** DCP EQUATION  
**Table type:** REFERENCE  
**Primary key:** `DCP_EQUATION_ID`  
**Columns:** 19  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALLPOSITION_IND` | DOUBLE | NOT NULL |  | All Position IndicatorColumn |
| 3 | `BEGIN_AGE_FLAG` | DOUBLE |  |  | identifies what the begin age is (hrs, days, wks, etc.) Column |
| 4 | `BEGIN_AGE_NBR` | DOUBLE |  |  | The number of days, weeks, months, etcColumn |
| 5 | `CALCVALUE_DESCRIPTION` | VARCHAR(100) |  |  | the label for the calculated valueColumn |
| 6 | `DCP_EQUATION_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the equationColumn |
| 7 | `DESCRIPTION` | VARCHAR(100) |  |  | The name of the equationColumn |
| 8 | `DESCRIPTION_KEY` | VARCHAR(100) |  |  | the name of the equationColumn |
| 9 | `END_AGE_FLAG` | DOUBLE |  |  | identifies what the end age is (hrs, days, wks, etc.) Column |
| 10 | `END_AGE_NBR` | DOUBLE |  |  | the number of weeks, days, etcColumn |
| 11 | `EQUATION_CODE` | VARCHAR(250) |  |  | A code determined by the tool that is used to identify the equationColumn |
| 12 | `EQUATION_DISPLAY` | VARCHAR(250) |  |  | The equation string that the user has typed into (a + b)Column |
| 13 | `EQUATION_MEANING` | VARCHAR(12) |  |  | A hardcode value to identify the equationColumn |
| 14 | `GENDER_CD` | DOUBLE | NOT NULL |  | the code that uniquely identifies a genderColumn |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DCP_EQUA_COMPONENT](DCP_EQUA_COMPONENT.md) | `DCP_EQUATION_ID` |
| [DCP_EQUA_POSITION](DCP_EQUA_POSITION.md) | `DCP_EQUATION_ID` |

