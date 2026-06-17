# PFT_ENCNTR_FACT

> ProFit encounter fact table persists all active encounters

**Description:** ProFit Encounter Fact  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BILLING_ENTITY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the related Billing Entity for this ENCNTR fact |
| 2 | `CLIENT_NUMBER_TXT_KEY` | VARCHAR(20) |  |  | The textual description of the Client number |
| 3 | `COLL_SEND_DT_TM` | DATETIME |  |  | Date that the ENCOUNTER was sent to a collection agency |
| 4 | `DUNNING_LEVEL_CD` | DOUBLE | NOT NULL |  | Code value indicating collections state that a ProFit encounter is in. |
| 5 | `ENCNTR_FIN_CLASS_CD` | DOUBLE | NOT NULL |  | The financial classification used for a given encounter. Examples may include Worker's Comp, Self Pay, etc. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Identifies the ENCOUNTER relation to the ENCOUNTER fact. |
| 7 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. |
| 8 | `HEALTH_PLAN_TYPE_CD` | DOUBLE | NOT NULL |  | Health plan type code identifies the type of health plan. (For example, PPO, HMW, Medicade, Medicare, etc.) |
| 9 | `LAST_ADJUSTMENT_AMT` | DOUBLE | NOT NULL |  | The last adjustment amount made on the ProFit encounter. |
| 10 | `LAST_ADJUSTMENT_DT_TM` | DATETIME |  |  | Date of the last adjustment made against this encounter |
| 11 | `LAST_ADJ_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Last Adjustment Transaction Sub Type |
| 12 | `LAST_PAYMENT_AMT` | DOUBLE | NOT NULL |  | The last payment amount on the ProFit encounter. |
| 13 | `LAST_PAYMENT_DT_TM` | DATETIME |  |  | Stores the last payment date and time |
| 14 | `LAST_PAY_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Last Payment Transaction Sub Type |
| 15 | `LAST_STMT_DT_TM` | DATETIME |  |  | Date of the last Statement made against this encounter |
| 16 | `PFT_ENCNTR_FACT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies each ENCOUNTER fact |
| 17 | `PFT_ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Identifies the associated ENCOUNTER as related to the ENCOUNTER fact |
| 18 | `PRE_COLL_SEND_DT_TM` | DATETIME |  |  | Date that the ENCOUNTER was sent to a collection agency |
| 19 | `PRIMARY_HP_ID` | DOUBLE | NOT NULL | FK→ | The associated primary health plan for this fact |
| 20 | `QUALIFIER_CD` | DOUBLE | NOT NULL |  | Allows a user-defined qualifier to be attached to each ProFit financial encounter. |
| 21 | `SECONDARY_HP_ID` | DOUBLE | NOT NULL | FK→ | The associated secondary health plan for this fact |
| 22 | `TERTIARY_HP_ID` | DOUBLE | NOT NULL | FK→ | The associated tertiary health plan for this fact |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 28 | `VIP_CD` | DOUBLE | NOT NULL |  | The VIP code indicates for this encounter that the person is to be identified and possibly treated with special consideration during the active time of the encounter. (i.e., employee, board member, famous person). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BILLING_ENTITY_ID` | [BILLING_ENTITY](BILLING_ENTITY.md) | `BILLING_ENTITY_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PFT_ENCNTR_ID` | [PFT_ENCNTR](PFT_ENCNTR.md) | `PFT_ENCNTR_ID` |
| `PRIMARY_HP_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `SECONDARY_HP_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `TERTIARY_HP_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |

