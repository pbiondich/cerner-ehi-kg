# PROXY

> Table for storing proxy relationship

**Description:** Table for storing proxy relationships  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `GROUP_PROXY_ID` | DOUBLE | NOT NULL | FK→ | This item is the value of the unique primary identifier of the prsnl_group_reltn table. It is an internal assigned number. |
| 5 | `MSG_CATEGORY_ID` | DOUBLE | NOT NULL |  | This is a Message Category code from the NOTIFICATION TYPE Code Set ( 3404 ) |
| 6 | `MSG_ITEM_GRP_ID` | DOUBLE | NOT NULL |  | This is a Message Item Group Code from the NOTIFICATION SUB TYPE Code Set ( 3405 ) |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 8 | `PROXY_ID` | DOUBLE | NOT NULL |  | The unique index for a row on this table. |
| 9 | `PROXY_PERSON_ID` | DOUBLE | NOT NULL |  | This column stores the identifier of the user that has been declared a proxy. |
| 10 | `PROXY_TYPE_CD` | DOUBLE | NOT NULL |  | The code value for the type of proxy relationship that a row on this table represents. |
| 11 | `TAKE_PROXY_STATUS_FLAG` | DOUBLE |  |  | Status flag of the Take Proxy row. 0 or NULL = not a take proxy row; 1 = Another user can take proxy; 2 = Another user has taken proxy; 3 = User acknowledges proxy was taken |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GROUP_PROXY_ID` | [PRSNL_GROUP_RELTN](PRSNL_GROUP_RELTN.md) | `PRSNL_GROUP_RELTN_ID` |

