# PFT_CHARGE_GLOBAL_DAYS

> Stores the charge related information which qualifies for the global billing.

**Description:** ProFit Charge Global Days  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related encounter record. |
| 3 | `GLOBAL_DAYS` | DOUBLE | NOT NULL |  | Once a person has a medical procedure, there is a period of time that if that same person were to come back to the hospital for the same procedure within a given time frame the services will not be covered by insurance. This timeframe is referred to as global days. |
| 4 | `GLOBAL_DAYS_END_DT_TM` | DATETIME | NOT NULL |  | Contains the service date plus the global days. |
| 5 | `MOD_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Stores the CPT modifier nomenclature identifier |
| 6 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related organization. |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely Identifies the related person. |
| 8 | `PFT_CHARGE_GLOBAL_DAYS_ID` | DOUBLE | NOT NULL |  | Uniquely identifies charge related information that qualifies for the global billing. |
| 9 | `PFT_CHARGE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies a related ProFit charge. |
| 10 | `PROC_NOMEN_ID` | DOUBLE | NOT NULL | FK→ | Stores the HCPCS/CPT Nomenclature Identifier |
| 11 | `SERVICE_DT_TM` | DATETIME |  |  | Stores the service date on which the charge is dropped. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `VERIFY_PHYS_ID` | DOUBLE | NOT NULL | FK→ | Stores the verifying physician identifier |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `MOD_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PFT_CHARGE_ID` | [PFT_CHARGE](PFT_CHARGE.md) | `PFT_CHARGE_ID` |
| `PROC_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `VERIFY_PHYS_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

