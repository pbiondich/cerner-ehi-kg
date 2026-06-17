# CHART_XENCNTR_FORMAT

> chart_xencntr_format

**Description:** This table defines the attributes for a cross encounter summary section.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 33

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIT_DT_LBL` | VARCHAR(32) |  |  | admit date column label |
| 6 | `ADMIT_DT_ODR` | DOUBLE |  |  | the order of admit date column |
| 7 | `BUILDING_LBL` | VARCHAR(32) |  |  | building column label |
| 8 | `BUILDING_ODR` | DOUBLE |  |  | the order of building column |
| 9 | `CHART_GROUP_ID` | DOUBLE | NOT NULL | FK→ | This is a unique number that identifies a chart group |
| 10 | `CLIENT_LBL` | VARCHAR(32) |  |  | client column label |
| 11 | `CLIENT_ODR` | DOUBLE |  |  | the order of client column |
| 12 | `DIAGNOSIS_LBL` | VARCHAR(32) |  |  | admitting diagnosis column label |
| 13 | `DIAGNOSIS_ODR` | DOUBLE |  |  | the order of admitting diagnosis column |
| 14 | `DISCHG_DT_LBL` | VARCHAR(32) |  |  | discharge date column label |
| 15 | `DISCHG_DT_ODR` | DOUBLE |  |  | the order of discharge date column |
| 16 | `EA_PREFIX_FORMAT` | VARCHAR(15) |  |  | encounter alias format |
| 17 | `EA_PREFIX_FORMAT_FLAG` | DOUBLE |  |  | encounter alias format flag |
| 18 | `ENCNTR_ALIAS_LBL` | VARCHAR(32) |  |  | encounter alias column label |
| 19 | `ENCNTR_ALIAS_ODR` | DOUBLE |  |  | the order of encounter alias column |
| 20 | `FACILITY_LBL` | VARCHAR(32) |  |  | facility column label |
| 21 | `FACILITY_ODR` | DOUBLE |  |  | the order of facility column |
| 22 | `FIN_NBR_LBL` | VARCHAR(32) |  |  | finacial number column label |
| 23 | `FIN_NBR_ODR` | DOUBLE |  |  | the order of finacial number column |
| 24 | `MRN_LBL` | VARCHAR(32) |  |  | medical record number column label |
| 25 | `MRN_ODR` | DOUBLE |  |  | the order of medical record number column |
| 26 | `NURSE_UNIT_LBL` | VARCHAR(32) |  |  | nurse unit column label |
| 27 | `NURSE_UNIT_ODR` | DOUBLE |  |  | the order of nurse unit column |
| 28 | `RSLT_SEQ_FLAG` | DOUBLE |  |  | sort sequence flag for encounters |
| 29 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 30 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 31 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 32 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 33 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_GROUP_ID` | [CHART_GROUP](CHART_GROUP.md) | `CHART_GROUP_ID` |

