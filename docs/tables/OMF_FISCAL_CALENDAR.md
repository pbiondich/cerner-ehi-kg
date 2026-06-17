# OMF_FISCAL_CALENDAR

> omf_fiscal_calendar

**Description:** Contains the fiscal date data from the OMF general ledger interface.  
**Table type:** REFERENCE  
**Primary key:** `OMF_FISCAL_CALENDAR_ID`  
**Columns:** 20  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_DT_NBR` | DOUBLE |  |  | beg_dt_nbr |
| 3 | `BEG_DT_TM` | DATETIME |  |  | Begin Date and Time value |
| 4 | `END_DT_NBR` | DOUBLE |  |  | end_dt_nbr |
| 5 | `END_DT_TM` | DATETIME |  |  | end_dt_tm |
| 6 | `FISCAL_PER` | DOUBLE |  |  | fiscal_per |
| 7 | `FISCAL_PER_YR` | VARCHAR(10) |  |  | fiscal_per_yr |
| 8 | `FISCAL_QTR` | DOUBLE |  |  | fiscal_qtr |
| 9 | `FISCAL_QTR_YR` | VARCHAR(10) |  |  | fiscal_qtr_yr |
| 10 | `FISCAL_YR` | DOUBLE |  |  | fiscal_yr |
| 11 | `INTERVAL_TYPE_CD` | DOUBLE | NOT NULL |  | interval_type_cd |
| 12 | `INTERVAL_VALUE` | DOUBLE |  |  | interval_value |
| 13 | `NBR_PERIODS` | DOUBLE |  |  | nbr_periods |
| 14 | `OMF_FISCAL_CALENDAR_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the omf_fiscal_calendar table. |
| 15 | `PREV_OMF_FISCAL_CALENDAR_ID` | DOUBLE | NOT NULL |  | prev_omf_Fiscal_calendar_id |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [OMF_ACC_FACT](OMF_ACC_FACT.md) | `OMF_FISCAL_DATE_ID` |
| [OMF_ACR_FACT](OMF_ACR_FACT.md) | `OMF_FISCAL_DATE_ID` |
| [OMF_BLS_FACT](OMF_BLS_FACT.md) | `OMF_FISCAL_DATE_ID` |
| [OMF_ICS_BDGT](OMF_ICS_BDGT.md) | `OMF_FISCAL_DATE_ID` |
| [OMF_ICS_FACT](OMF_ICS_FACT.md) | `OMF_FISCAL_DATE_ID` |

