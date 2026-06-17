# RC_SLA_RULE

> Contains service level agreement rules for health plans and payers.

**Description:** Revenue Cycle Service Level Agreement Rule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | The activity sub type code for the SLA Rule |
| 3 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the code defining the type of activity for this service level agreement. |
| 4 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the code defining the catalog type for this service level agreement. |
| 5 | `ENCOUNTER_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the code defining the type of encounter for this service level agreement. |
| 6 | `FACILITY_CD` | DOUBLE | NOT NULL |  | This column is misnamed and actually contains organization_id. If it is 0, that means all organizations |
| 7 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Health Plan related to this record. |
| 8 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL |  | Contains the code defining the order catalog for this service level agreement. |
| 9 | `ORDER_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related order synonym for this record. |
| 10 | `PAYER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the organization for the payer of this service level agreement. |
| 11 | `RC_SLA_RULE_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RC_SLA_RULE table. |
| 12 | `SLA_BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The Begin effective date for the service level agreement. |
| 13 | `SLA_END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The End effective date for the service level agreement. |
| 14 | `SLA_UNIT_CD` | DOUBLE | NOT NULL |  | Identifies the units for the service level agreement value. |
| 15 | `SLA_VALUE` | DOUBLE | NOT NULL |  | Contains the Value of this Service Level Agreement. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `WEEKEND_CD` | DOUBLE | NOT NULL |  | Contains a yes/no code for whether or not t weekends are taken into account. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `ORDER_SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `PAYER_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

