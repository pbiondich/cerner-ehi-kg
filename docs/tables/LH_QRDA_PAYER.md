# LH_QRDA_PAYER

> This table is used to store elements that are used to create the Payer Section in the body of a QRDA file for submission

**Description:** LH_QRDA_PAYER  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 2 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was first loaded into the table. |
| 3 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 4 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 5 | `INSRNCE_GRP_NBR` | DOUBLE |  |  | The group or contract number related to the insurance policy or program |
| 6 | `INSRNCE_NAME` | VARCHAR(50) |  |  | The name of the insurance company |
| 7 | `INSRNCE_PLAN_TYPE` | VARCHAR(50) |  |  | The plan type of the insurance (e.g. PI for Private Insurance) |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time the record was last loaded into the table. |
| 9 | `LH_QRDA_PAYER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_PAYER table. |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Payer section is related (i.e. lh_qrda_pqrs_id) |
| 12 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The value of the primary identifier of millennium source table |
| 13 | `PARENT_ENTITY_NAME` | VARCHAR(50) |  |  | The name of the table this Payer section is related (i.e. LH_QRDA_PQRS) |
| 14 | `PARENT_ENTITY_NAME2` | VARCHAR(50) | NOT NULL |  | The name of millennium source table |
| 15 | `PAYER_ID` | DOUBLE | NOT NULL |  | Unique identifier for lighthouse PQRS QRDA Payer section |
| 16 | `POLICY_TYPE` | VARCHAR(50) |  |  | The policy or program coverage role type (e.g. 'Self') |
| 17 | `POLICY_TYPE_DISPLAY` | VARCHAR(500) |  |  | Text description of the policy type |
| 18 | `POLICY_TYPE_SYSTEM` | VARCHAR(50) |  |  | String representation of the code system that policy_type was derived from |
| 19 | `POLICY_TYPE_SYSTEM_NAME` | VARCHAR(50) |  |  | Represents the codeSystem string of the code node |
| 20 | `POLICY_TYPE_SYSTEM_SDTC` | VARCHAR(200) |  |  | OID of codeSystem string. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 24 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

