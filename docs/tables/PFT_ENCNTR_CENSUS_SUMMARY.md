# PFT_ENCNTR_CENSUS_SUMMARY

> Summary of Encounter Level census information

**Description:** ProFit Encounter Census Summary  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOMMODATION_CD` | DOUBLE | NOT NULL |  | Current type of accommodations in which the patient (encounter) has been placed. (e.g. Private, Semi Private, etc.) |
| 2 | `ADMIT_CNT` | DOUBLE |  |  | The number of patient admits for the time period |
| 3 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the related Billing Entity for an encounter census summary |
| 4 | `DISCHARGE_CNT` | DOUBLE |  |  | The number of patient discharges for the time period |
| 5 | `ENCNTR_TYPE_CLASS_CD` | DOUBLE | NOT NULL |  | Used to categorize patients into more general groups than encounter type. (i.e., inpatient, outpatient, emergency, recurring outpatient). Code values have Cerner defined meanings. |
| 6 | `FIN_CLASS_CD` | DOUBLE | NOT NULL |  | Financial classification used for a given encounter. Examples may include Worker's Comp, Self Pay, etc. |
| 7 | `LOC_BUILDING_CD` | DOUBLE | NOT NULL | FK→ | Current patient location with a location type of building |
| 8 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Current patient location with a location type of facility |
| 9 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Current patient location with a location type of Nurse Unit |
| 10 | `MED_SERVICE_CD` | DOUBLE | NOT NULL |  | Type or Category of medical service that patient receives in relation to the encounter. The category may be of treatment type, surgery, general resources, or others. |
| 11 | `PATIENT_DAYS_CNT` | DOUBLE |  |  | Number of inpatient patient care days for the time period |
| 12 | `PFT_ENCNTR_CENSUS_SUMMARY_ID` | DOUBLE | NOT NULL |  | Identifies a Summary of encounter census-level Information |
| 13 | `PFT_FISCAL_PERIOD_ID` | DOUBLE | NOT NULL | FK→ | This identifies which fiscal period the transaction was posted against. This column is constrained by the PFT_FISCAL_PERIOD table. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 19 | `VISIT_DAYS_CNT` | DOUBLE |  |  | The number of outpatient visits for the time period. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `LOC_BUILDING_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `PFT_FISCAL_PERIOD_ID` | [PFT_FISCAL_PERIOD](PFT_FISCAL_PERIOD.md) | `PFT_FISCAL_PERIOD_ID` |

