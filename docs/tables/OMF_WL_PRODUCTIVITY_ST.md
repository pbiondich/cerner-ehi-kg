# OMF_WL_PRODUCTIVITY_ST

> omf_wl_productivity_st

**Description:** Workload productivity stats  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CPT_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the cpt code. |
| 2 | `DRG_NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | The unique identifier for the DRG code. |
| 3 | `EXTENDED_UNITS` | DOUBLE |  |  | The quantity * units * multiplier. |
| 4 | `MULTIPLIER` | DOUBLE |  |  | The raw number of units that were assigned based on the standard or the number of units entered in the Pricing Tool. |
| 5 | `NBR_CPT_PROCS` | DOUBLE |  |  | The summarized number of cpt procedures. |
| 6 | `NBR_DRGS` | DOUBLE |  |  | The summarized number of DRGs |
| 7 | `NBR_ICD_PROCS` | DOUBLE |  |  | The summarized number of icd procedures. |
| 8 | `OMF_WL_PRODUCTIVITY_ST_ID` | DOUBLE | NOT NULL |  | The unique identifier for the omf_wl_productivity_st table. |
| 9 | `ORD_PHYS_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the ordering physician. |
| 10 | `PROJ_WORKLOAD` | DOUBLE |  |  | The projected number of workload units. |
| 11 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the performing personnel. |
| 12 | `PRSNL_POSITION_CD` | DOUBLE | NOT NULL |  | The position of the prsnl. |
| 13 | `QTY` | DOUBLE |  |  | The quantity for the number of units that will be multiplied to the workload multiplier in order to determine the volume of workload. |
| 14 | `RAW_COUNT` | DOUBLE |  |  | Raw procedure count. |
| 15 | `SERVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Codified field which identifies the current category of service the patient is receiving for this encounter. |
| 16 | `SERVICE_DT_NBR` | DOUBLE |  |  | The Julian date number on which the service was complete for the event that resulted in this workload row. |
| 17 | `UNITS` | DOUBLE |  |  | The number of units that were calculated by the server using the multiplier and interval logic if necessary. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORD_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

