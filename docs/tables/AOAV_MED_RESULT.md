# AOAV_MED_RESULT

> Activity table to store the medication results that attributed to a patient's outcomes

**Description:** AOAV_MEDICATION_RESULT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_DOSAGE` | DOUBLE |  |  | The actual volume or quantity of administration. |
| 6 | `ADMIN_DT_TM` | DATETIME |  |  | The tme at which the medication administration became active or the time that the administration happened. |
| 7 | `ADMIN_ROUTE_CD` | DOUBLE | NOT NULL |  | The route of administration. |
| 8 | `AOAV_COMP_CD` | DOUBLE | NOT NULL |  | Code value for a component |
| 9 | `AOAV_MED_RESULT_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 10 | `CALCULATED_FLAG` | DOUBLE |  |  | The calculated flag giving the state of the event.0-Needs to be calculated; 1- calculation in progress; 2-calculation done |
| 11 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Foreign key to the order_catalog table which has column CATALOG_CD as its primary key (FK from CODE_VALUE) |
| 12 | `DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measurement for dosage. |
| 13 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Foreign key value from the encounter table. |
| 14 | `ERROR_STATUS_FLAG` | DOUBLE |  |  | The error status flag (0 = no error, 1 = in error, 2 = invalid) |
| 15 | `EVENT_ID` | DOUBLE | NOT NULL |  | EVENT_ID from the CLINICAL_EVENT table |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE ** This field is no longer used - DBARCHDTL-23349 |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |

