# REACTION

> The Reaction table is used to record past adverse reactions regarding an allergy for a person.

**Description:** Reaction  
**Table type:** ACTIVITY  
**Primary key:** `REACTION_ID`  
**Columns:** 27  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALLERGY_ID` | DOUBLE | NOT NULL | FK→ | Uniquely defines an allergy/adverse reaction within the allergy table. The allergy_id can be associated with multiple allergy instances. When a new allergy is added to the allergy table the allergy_id is assigned to the allergy_instance_id. |
| 6 | `ALLERGY_INSTANCE_ID` | DOUBLE | NOT NULL |  | Unique identifier for the allergy table. Each change or revision made to an allergy/adverse reaction creates a new allergy instance. |
| 7 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 8 | `CMB_DT_TM` | DATETIME |  |  | Date/Time the item was combined |
| 9 | `CMB_FLAG` | DOUBLE | NOT NULL |  | Flag indicating the combined status of the item. 0 = not part of combined, 1 Combined, 2 Historically Combined, 3 Continuation of Combine indication |
| 10 | `CMB_PERSON_ID` | DOUBLE | NOT NULL |  | Person identifier of the "From" person being combined |
| 11 | `CMB_PRSNL_ID` | DOUBLE | NOT NULL |  | Person identifier who performed the combined |
| 12 | `CMB_REACTION_ID` | DOUBLE | NOT NULL |  | The "From" person's reaction identifier of the reaction being combined |
| 13 | `CMB_TZ` | DOUBLE |  |  | Combine Date Time ZoneColumn |
| 14 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 15 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 16 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 17 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 18 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 19 | `REACTION_FTDESC` | VARCHAR(255) |  |  | A free text description of the reaction. |
| 20 | `REACTION_ID` | DOUBLE | NOT NULL | PK | Unique identifier of the reaction table. |
| 21 | `REACTION_NOM_ID` | DOUBLE | NOT NULL |  | Unique identifier of the reaction. |
| 22 | `SEVERITY_CD` | DOUBLE | NOT NULL |  | Severity of the reaction, exmaples include low, mild, moderate and high etc¿ comes from code set 4646006 |
| 23 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALLERGY_ID` | [ALLERGY](ALLERGY.md) | `ALLERGY_INSTANCE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [REACT_ENTITY_RELTN](REACT_ENTITY_RELTN.md) | `REACTION_ID` |

