# CRIMINAL_CHARGES_DISP_R

> The associated court disposition for a criminal charge of an encounter.

**Description:** Criminal Charges Disposition Relation  
**Table type:** ACTIVITY  
**Primary key:** `CRIMINAL_CHARGES_DISP_R_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COURT_DISPOSITION_CD` | DOUBLE | NOT NULL |  | The court's disposition for a criminal charge |
| 6 | `CRIMINAL_CHARGES_DISP_R_ID` | DOUBLE | NOT NULL | PK | Identifies the related associated court disposition for a criminal charge of an encounter. |
| 7 | `OUTSTANDING_CHARGES_R_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated charge(s) related to an Encounter. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OUTSTANDING_CHARGES_R_ID` | [ENCNTR_CRIMINAL_CHARGES_R](ENCNTR_CRIMINAL_CHARGES_R.md) | `OUTSTANDING_CHARGES_R_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CRIMINAL_CHRGS_DISP_HIST](CRIMINAL_CHRGS_DISP_HIST.md) | `CRIMINAL_CHARGES_DISP_R_ID` |

