# VISITCODING_AUDIT

> The root for a charging audit trail serving as a pointer to the list of coding extracts used to suggest a charge and the coding extract used to generate the final charge.

**Description:** Coding Audit  
**Table type:** ACTIVITY  
**Primary key:** `VISITCODING_AUDIT_ID`  
**Columns:** 22  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPLIED_CHARGE_ID` | DOUBLE | NOT NULL | FK→ | The nomenclature_id of the charge code that was applied by the coder. |
| 2 | `APPLIED_MODIFIER_ID` | DOUBLE | NOT NULL | FK→ | ** OBSOLETE ** THIS COLUMN IS NOT USED AND WILL BECOME OBSOLETE WITH CHANGE MADE BY CR 1-3060766751 - FEB. 2009 ** Nomenclature id of the modifier applied to the charge |
| 3 | `AUDIT_STATUS_CD` | DOUBLE | NOT NULL |  | Visitcoding status [in progress, not started, signed] |
| 4 | `AUTOMATED_DELTA_IND` | DOUBLE | NOT NULL |  | Automated Delta Indicator |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHARGE_DT_TM` | DATETIME | NOT NULL |  | Date when the charge was generated. |
| 7 | `CODER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl.person_id of the coder |
| 8 | `CRITICAL_CARE_IND` | DOUBLE | NOT NULL |  | Indicates if this coding audit had critical care yes selected. |
| 9 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter.encntr_id |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `NO_CHARGE_IND` | DOUBLE | NOT NULL |  | indicates the charge was dropped as a no charge charge |
| 12 | `PREV_VISITCODING_AUDIT_ID` | DOUBLE | NOT NULL | FK→ | Previous (original) valid tracking audit row. Used for type-2 Versioning of the tracking audit row |
| 13 | `PRIMARY_NOMENCLATURE_ID` | DOUBLE | NOT NULL | FK→ | FOREIGN KEY VALUE FROM NOMENCLATURE |
| 14 | `PROVIDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Prsnl.person_id of the care provider for whom the charge was created |
| 15 | `SUGGESTED_CHARGE_ID` | DOUBLE | NOT NULL | FK→ | The nomenclature_id of the charge code that was suggested to the coder. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 21 | `VISITCODE_RULESET_ID` | DOUBLE | NOT NULL | FK→ | Coding ruleset used to suggest the charge |
| 22 | `VISITCODING_AUDIT_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `APPLIED_CHARGE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `APPLIED_MODIFIER_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `CODER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PREV_VISITCODING_AUDIT_ID` | [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `VISITCODING_AUDIT_ID` |
| `PRIMARY_NOMENCLATURE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PROVIDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SUGGESTED_CHARGE_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `VISITCODE_RULESET_ID` | [VISITCODE_RULESET](VISITCODE_RULESET.md) | `VISITCODE_RULESET_ID` |

## Referenced by (6)

| From table | Column |
|------------|--------|
| [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `PREV_VISITCODING_AUDIT_ID` |
| [VISITCODING_BILLITEM](VISITCODING_BILLITEM.md) | `VISITCODING_AUDIT_ID` |
| [VISITCODING_DX](VISITCODING_DX.md) | `VISITCODING_AUDIT_ID` |
| [VISITCODING_EXTRACT](VISITCODING_EXTRACT.md) | `VISITCODING_AUDIT_ID` |
| [VISITCODING_MODIFIER](VISITCODING_MODIFIER.md) | `VISITCODING_AUDIT_ID` |
| [VISITCODING_PROVIDER](VISITCODING_PROVIDER.md) | `VISITCODING_AUDIT_ID` |

