# LH_F_REST_DTL_METRICS

> Fact table for Restraint Management Detail Lighthouse Reporting

**Description:** LH_F_REST_DTL_METRICS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 47

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADVERSE_IND` | DOUBLE |  |  | Identifies if the an adverse event was document during restraint episode |
| 3 | `ADV_AGITATION_IND` | DOUBLE |  |  | Identifies if the agitation adverse event was document during restraint episode |
| 4 | `ADV_ESCALATION_IND` | DOUBLE |  |  | Identifies if the escalation of injuryois behavior adverse event was document during restraint episode |
| 5 | `ADV_FALL_IND` | DOUBLE |  |  | Identifies if the injury related to fall adverse event was document during restraint episode |
| 6 | `ADV_IMP_CIRCULATION_IND` | DOUBLE |  |  | Identifies if the impaired circulation adverse event was document during restraint episode |
| 7 | `ADV_REDUCTION_FUNC_IND` | DOUBLE |  |  | Identifies if the severe reduction in fucnctional capacity adverse event was document during restraint episode |
| 8 | `ADV_SKIN_BREAK_IND` | DOUBLE |  |  | Identifies if the skin breakdown adverse event was document during restraint episode |
| 9 | `D_REST_BUILDING_ID` | DOUBLE | NOT NULL | FK→ | The building in which the patient is restrained. |
| 10 | `D_REST_FACILITY_ID` | DOUBLE | NOT NULL | FK→ | The facility in which the patient is restrained. |
| 11 | `D_REST_NURSE_UNIT_ID` | DOUBLE | NOT NULL | FK→ | The nurse_unit in which the patient is restrained. |
| 12 | `ENCNTR_ID` | DOUBLE | NOT NULL |  | Identifies the encounter against which the quality measure is associated. Foreign key to the ENCOUNTER table. |
| 13 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 14 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 15 | `F_REST_DTL_METRICS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_F_REST_DTL_METRICS table. |
| 16 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 17 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the unique source within the delivery network responsible for supplying the data. |
| 18 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 19 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for the logical domain. This identifier allows the data to be grouped by logical domain. |
| 20 | `NONVIO_ASSESS_EXCL_IND` | DOUBLE |  |  | Identifies the restraint episode is excluded for restraint non-violent assessment for continued need |
| 21 | `NONVIO_ASSESS_IND` | DOUBLE |  |  | Identifies the patient has assessment of nonviolent behavior continued performed with designated time frame during restraint episode |
| 22 | `NONVIO_INIT_ORD_IND` | DOUBLE |  |  | Identifies patient has restraint initiation nonviolent order placed with design time frame during restraint episode |
| 23 | `NONVIO_RENEW_EXCL_IND` | DOUBLE |  |  | Identifies the restraint episode is excluded for restraint non-violent renew order |
| 24 | `NONVIO_RENEW_IND` | DOUBLE |  |  | Identifies patient has assessment of nonviolent behavior continued performed with designated time frame during restraint episode |
| 25 | `PARTITION_DT_TM` | DATETIME |  |  | The date/time the encounter was discharged. |
| 26 | `PHYS_CARE_EXCL_IND` | DOUBLE |  |  | Identifies the restraint episode is excluded for restraints released to provide physical care needs |
| 27 | `PHYS_CARE_IND` | DOUBLE |  |  | Identifies the patient has restraint released to provider physical care is in designated time frame during restraint episode |
| 28 | `RESTRAINT_BEG_DT_TM` | DATETIME |  |  | The date/time on which restraint activity for restraint episode beginning date/time |
| 29 | `RESTRAINT_BEG_UTC_DT_TM` | DATETIME |  |  | The date/time on which the restraint activity for restraint episode beginning datetime; normalized to GMT. |
| 30 | `RESTRAINT_BEH_FLAG` | DOUBLE |  |  | Identifies the restraint initialization behavior reason for violent or non-violent or other was documented during restraint episode (none/other , violent, non-violent) |
| 31 | `RESTRAINT_END_DT_TM` | DATETIME |  |  | The Date/time on which the restraint discontinue for restraint episode end datetime |
| 32 | `RESTRAINT_END_UTC_DT_TM` | DATETIME |  |  | The Date/time on which the restraint discontinue for restraint episode end datetime; normalized to GMT |
| 33 | `REST_PHYS_DT_TM` | DATETIME |  |  | The date/time on which physical restraint type was document during restraint episode |
| 34 | `REST_PHYS_UTC_DT_TM` | DATETIME |  |  | The date/time on which physical restraint type was document during restraint episode; normalized to GMT |
| 35 | `REST_SEC_DT_TM` | DATETIME |  |  | The date/time on which seclusion restraint type was document during restraint episode |
| 36 | `REST_SEC_UTC_DT_TM` | DATETIME |  |  | The date/time on which seclusion restraint type was document during restraint episode; normalized to GMT |
| 37 | `RISK_PRIOR_RESTRAINT_IND` | DOUBLE |  |  | Identifies if the patient was at risk prior to this restraint episode beginning |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 40 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 41 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 42 | `VIO_ASSESS_IND` | DOUBLE |  |  | Identifies patient has face to face assessment of violent behavior performed with 1 hours of initiation of restraint |
| 43 | `VIO_INIT_ORD_DT_TM` | DATETIME |  |  | The date/time on which the restraint initiation violent order placed with design time frame during restraint episode |
| 44 | `VIO_INIT_ORD_IND` | DOUBLE |  |  | Identifies patient has restraint initiation violent order placed with design time frame during restraint episode |
| 45 | `VIO_INIT_ORD_UTC_DT_TM` | DATETIME |  |  | The date/time on which the restraint initiation violent order placed with design time frame during restraint episode; normalized to GMT |
| 46 | `VIO_REORD_EXCL_IND` | DOUBLE |  |  | INDICATOR |
| 47 | `VIO_REORD_IND` | DOUBLE |  |  | Identifies patient has restraint violent re-order at appropriate intervals during the restraint episode |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `D_REST_BUILDING_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `D_BUILDING_ID` |
| `D_REST_FACILITY_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `D_FACILITY_ID` |
| `D_REST_NURSE_UNIT_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `D_NURSE_UNIT_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_BUILDING](LH_D_BUILDING.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_FACILITY](LH_D_FACILITY.md) | `HEALTH_SYSTEM_SOURCE_ID` |
| `HEALTH_SYSTEM_SOURCE_ID` | [LH_D_NURSE_UNIT](LH_D_NURSE_UNIT.md) | `HEALTH_SYSTEM_SOURCE_ID` |

