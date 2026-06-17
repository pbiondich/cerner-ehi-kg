# DCP_ENTITY_RELTN

> Table is used to store the relationship between any two _id or _cd entities in the system.

**Description:** DCP ENTITY RELATIONSHIP  
**Table type:** REFERENCE  
**Primary key:** `DCP_ENTITY_RELTN_ID`  
**Columns:** 20  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME |  |  | The beginning effective date of this relationship. |
| 3 | `DCP_ENTITY_RELTN_ID` | DOUBLE | NOT NULL | PK | The id of this relationship. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ENTITY1_DISPLAY` | VARCHAR(100) |  |  | The display value for entity 1 of the relationship. |
| 6 | `ENTITY1_ID` | DOUBLE | NOT NULL |  | The id of entity 1 of the relationship. |
| 7 | `ENTITY1_NAME` | CHAR(32) |  |  | First entity name |
| 8 | `ENTITY2_DISPLAY` | VARCHAR(100) |  |  | The display value of entity2 of the relationship. |
| 9 | `ENTITY2_ID` | DOUBLE | NOT NULL |  | The id of the second entity in the relationship. |
| 10 | `ENTITY2_NAME` | CHAR(32) |  |  | Second entity name |
| 11 | `ENTITY3_DISPLAY` | VARCHAR(100) |  |  | The display value of entity3 of the relationship. |
| 12 | `ENTITY3_ID` | DOUBLE |  |  | The id of entity 3 of the relationship. |
| 13 | `ENTITY3_NAME` | VARCHAR(32) |  |  | Third entity name. |
| 14 | `ENTITY_RELTN_MEAN` | VARCHAR(12) |  |  | The meaning of the relationship that is used to identify the source of entity1 and entity2. |
| 15 | `RANK_SEQUENCE` | DOUBLE |  |  | A sequence number to place the relationships in a hierarchy. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (5)

| From table | Column |
|------------|--------|
| [ALERT_AUDIT_ALLERGY](ALERT_AUDIT_ALLERGY.md) | `DCP_ENTITY_RELTN_ID` |
| [ALERT_AUDIT_DRUG](ALERT_AUDIT_DRUG.md) | `DCP_ENTITY_RELTN_ID` |
| [ALERT_AUDIT_DUP](ALERT_AUDIT_DUP.md) | `DCP_ENTITY_RELTN_ID` |
| [ALERT_AUDIT_FOOD](ALERT_AUDIT_FOOD.md) | `DCP_ENTITY_RELTN_ID` |
| [DRUG_CLASS_INT_CSTM_ENTITY_R](DRUG_CLASS_INT_CSTM_ENTITY_R.md) | `DCP_ENTITY_RELTN_ID` |

