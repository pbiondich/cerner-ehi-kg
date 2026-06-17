# ACCESS_CONTROL_POLICY

> This table stores policies used to determine a consumer's authorization decision based on the consumers's access control status.

**Description:** Access Control Policy  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESS_CONTROL_DECISION_CD` | DOUBLE | NOT NULL |  | The consumer's authorization decision. (I.E Permit or Deny) |
| 2 | `ACCESS_CONTROL_POLICY_ID` | DOUBLE | NOT NULL |  | The primary key of the ACCESS_CONTROL_POLICY table. |
| 3 | `ACCESS_CONTROL_POLICY_NAME` | VARCHAR(100) | NOT NULL |  | The name of the Access Control Policy |
| 4 | `ACCESS_CONTROL_POLICY_NAME_KEY` | VARCHAR(100) | NOT NULL |  | Identical to column Access_Control_Policy_Name except it is in all capitals with special characters and blanks removed. Used for indexing and searching for a policy by name. |
| 5 | `ACCESS_CONTROL_TYPE_ENTITY_ID` | DOUBLE | NOT NULL |  | The entity ID for the type of access control to which this policy applies. |
| 6 | `ACCESS_CONTROL_TYPE_ENTITY_NM` | VARCHAR(30) | NOT NULL |  | The entity name for the type of access control to which this policy applies. (I.e. CODE_VALUE) |
| 7 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `DATA_SOURCE_ENTITY_ID` | DOUBLE | NOT NULL |  | The entity ID for the data source that defines the policy. |
| 10 | `DATA_SOURCE_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The entity name for the data source that defines the policy.(i.e Contibutor_system, Organization) |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `STATUS_CD` | DOUBLE | NOT NULL |  | The access control status to which this policy applies. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

