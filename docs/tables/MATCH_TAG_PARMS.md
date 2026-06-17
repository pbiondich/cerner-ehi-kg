# MATCH_TAG_PARMS

> The match & tag parameter table contains processing parameters by contributor system. These parameters define which fields are used when attempting to find a match between the person on the incoming transaction and an existing person in the database.

**Description:** Match & Tag Parameters  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 25

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_ENTITY_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | This field represents the identifier type, such as internal identifier type or alias type. The specific code set for the identifier type varies and corresponds to the alias_entity_name attribute within the same row. |
| 6 | `ALIAS_ENTITY_NAME` | VARCHAR(32) |  |  | This field represents the parent table for which the alias identifier, internal identifier or other identifier type will be created or found. |
| 7 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL | FK→ | Alias pool code identifies a unique set or list of identifiers. |
| 8 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 9 | `BILLING_IND` | DOUBLE |  |  | Determines the value of the billing indicator (BILL_ORD_NBR_IND) on the order alias table. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL | FK→ | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `MATCH_FIELD_CD` | DOUBLE | NOT NULL |  | The identifier or demographic element that is used during the match or reconciliation process. |
| 13 | `MATCH_FUNCTION_CD` | DOUBLE | NOT NULL |  | The validation routine used during the match or reconciliation process, such as Order Match, GT1 Person Match, or Person Match (Authenticated Records). |
| 14 | `MATCH_SEQ` | DOUBLE | NOT NULL |  | Match Sequence |
| 15 | `MATCH_TAG_PARMS_ID` | DOUBLE | NOT NULL |  | Unique identifier for the MATCH_TAG_PARMS table. |
| 16 | `MATCH_VALIDATION_CD` | DOUBLE | NOT NULL |  | This code helps to determine what action will be performed if a field in the message does not match the same field of an existing row in a table. For example, Match Required or Warn Mismatch. |
| 17 | `OPF_IND` | DOUBLE |  |  | Indicates whether this match and tag parameter is used by OPF for its probabilistic matching routine. |
| 18 | `ORDER_CONTROL_CD` | DOUBLE | NOT NULL |  | Enables different order match criteria based on the order control code transmitted in the HL7 message. |
| 19 | `PRIM_ALIAS_IND` | DOUBLE |  |  | Used to identify the primary alias or identifier used for match processing. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 25 | `WEIGHT` | DOUBLE |  |  | Determines the weight given to the particular match and tag parameter as used by OPF for its probabilistic matching routine. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALIAS_POOL_CD` | [ALIAS_POOL](ALIAS_POOL.md) | `ALIAS_POOL_CD` |
| `CONTRIBUTOR_SYSTEM_CD` | [CONTRIBUTOR_SYSTEM](CONTRIBUTOR_SYSTEM.md) | `CONTRIBUTOR_SYSTEM_CD` |

