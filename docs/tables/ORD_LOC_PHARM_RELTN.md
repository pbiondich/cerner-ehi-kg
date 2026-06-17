# ORD_LOC_PHARM_RELTN

> Stores the association between various locations to corresponding pharmacies for a given pharmacy type. This table will be utilized by Orders and Plans services which will perform add, update and remove operations on the table. These services are primarily utilized by bedrock tool to associate facility/facilities with a pharmacy of given type. User can also update the association and remove this association throuugh the tool.

**Description:** Order Location Pharmacy Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `LOC_CD` | DOUBLE | NOT NULL | FK→ | Code value of the facility, building or nurse unit with which the pharmacy will be associated. Codeset: 220 |
| 4 | `ORD_LOC_PHARM_RELTN_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the ORD_LOC_PHARM_RELTN table. |
| 5 | `PHARM_IDENT` | VARCHAR(100) | NOT NULL |  | The Cerner millennium identifier for a pharmacy. |
| 6 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Code value of the type of the pharmacy that needs to be associated to the facility. Codeset: 4644007 |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOC_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

