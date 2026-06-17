# DISPENSE_HX_ALIAS

> Stores Dispense history alias from foreign dispensing system

**Description:** Dispense History Alias  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS` | VARCHAR(200) | NOT NULL |  | The system identifier for the record which originates from a foreign dispensing system. |
| 6 | `ALIAS_POOL_CD` | DOUBLE | NOT NULL |  | The alias pool code identifies a unique set or list of order identifiers. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DISPENSE_HX_ALIAS_ID` | DOUBLE | NOT NULL |  | Uniquely identifies the Dispense_Hx_Alias record that originated from a foreign system. |
| 9 | `DISPENSE_HX_ALIAS_TYPE_CD` | DOUBLE | NOT NULL |  | Type code which identifies the type of alias originating from the foreign system, e.g., dispense, order, etc. |
| 10 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | This field links the DISPENSE_HX_ALIAS record to the Dispensing event record. This will enable users to track each Inbound Alias to the appropriate Charge / Credit transaction. |
| 11 | `QUEUE_ID` | DOUBLE | NOT NULL |  | This field links the DISPENSE_HX_ALIAS record to the Pharmacy Queue Error record. This will enable users to track each Inbound Alias to the appropriate error record. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |

